import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
executable_path = r'C:\Users\user\Desktop\Fawaz\chromedriver.exe'
chrome_options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(executable_path=executable_path)


def get_rows_text():
    genel_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/ul/li[1]/a')
    portfolio_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/ul/li[2]/a')
    collection = []
    genel_table = driver.find_element_by_css_selector('#MainContent_GridViewGenel > tbody')
    portfolio_table = driver.find_element_by_css_selector('#MainContent_GridViewDagilim > tbody')
    genel_rows = genel_table.find_elements_by_tag_name('tr')[1:]
    portfolio_rows = portfolio_table.find_elements_by_tag_name('tr')[1:]
    

    for row in genel_rows:
        my_elements = []
        driver.execute_script("arguments[0].click();", genel_btn)
        cells = row.find_elements_by_tag_name('td')
        for cell in cells:
            my_elements.append(cell.text)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", portfolio_btn)
        time.sleep(2)
        adjacent_row = portfolio_rows[genel_rows.index(row)]
        adjacent_cells = adjacent_row.find_elements_by_tag_name('td')[3:]
        for cello in adjacent_cells:
            my_elements.append(cello.text)
    collection.append(my_elements)
    return collection

# def sub(genel_rows,genel_btn,portfolio_rows,portfolio_btn):
#     for row in genel_rows:
#         my_elements = []
#         driver.execute_script("arguments[0].click();", genel_btn)
#         cells = row.find_elements_by_tag_name('td')
#         for cell in cells:
#             my_elements.append(cell.text)
#         time.sleep(2)
#         driver.execute_script("arguments[0].click();", portfolio_btn)
#         time.sleep(2)
#         adjacent_row = portfolio_rows[genel_rows.index(row)]
#         adjacent_cells = adjacent_row.find_elements_by_tag_name('td')[3:]
        
#         for cell in adjacent_cells:
#             my_elements.append(cell.text)
#         return my_elements



# /html/body/form/div[3]/div[3]/div/div[4]/div[1]/table/tbody/tr/td[4]/input
# /html/body/form/div[3]/div[3]/div/div[4]/div[1]/table/tbody/tr/td[4]/input


def get_info(start_date,end_date):
    row_collection = []
    driver.get('https://www.tefas.gov.tr/TarihselVeriler.aspx')
    time.sleep(2)
    btn = driver.find_element_by_css_selector('#MainContent_ButtonSearchDates')
    portfolio_btn = driver.find_element_by_css_selector('#ui-id-2')
    time.sleep(4)
    input_box_one = driver.find_element_by_css_selector('#MainContent_TextBoxStartDate')
    input_box_two = driver.find_element_by_css_selector('#MainContent_TextBoxEndDate')
    input_box_one.clear()
    input_box_one.send_keys(start_date)
    input_box_two.clear()
    input_box_two.send_keys(end_date)
    driver.execute_script("arguments[0].click();", btn)
    headers = []
    time.sleep(2)
    header_text = driver.find_element_by_css_selector('#MainContent_GridViewGenel > tbody > tr.fund-grid-header')
    header_cells = header_text.find_elements_by_tag_name('th')
    for header_cell in header_cells:
        headers.append(header_cell.text)
    time.sleep(5)
    portfolio_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/ul/li[2]/a')
    driver.execute_script("arguments[0].click();", portfolio_btn)
    time.sleep(5)
    other_headers = driver.find_element_by_xpath('//*[@id="MainContent_GridViewDagilim"]/tbody/tr[1]')
    other_header_cells = other_headers.find_elements_by_tag_name('th')[3:]
    for header in other_header_cells:
        headers.append(header.text)
    result = get_rows_text()
    df = pd.DataFrame(result,columns=headers)
    df.to_csv(start_date+"  to  "+end_date+'.csv')

    

    



def get_data():
    print("Enter start date in format DD/MM/YY")
    # start_date = input()
    # start_date = start_date.strip().replace("/",".")
    print("Enter end date in format DD/MM/YY")
    # end_date = input()
    # end_date = end_date.strip().replace("/",".")
    # get_info(start_date,end_date)
    get_info('06.08.2020','06.08.2020')
    
get_data()
