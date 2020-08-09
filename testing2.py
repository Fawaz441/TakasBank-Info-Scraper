import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
executable_path = r'C:\Users\Fawaz\Desktop\Dowstrademus\chromedriver.exe'
chrome_options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(executable_path=executable_path)


def get_rows_text():
  
    genel_collection = []
    portfolio_collection = []
    
   

    for x in range(2):
      
        try:
            genel_table = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table')
            genel_rows = genel_table.find_elements_by_tag_name('tr')[1:]
            for row in genel_rows:
                print('genel row ..............',genel_rows.index(row))
                my_elements = []
                cells = row.find_elements_by_tag_name('td')
                for cell in cells:
                    my_elements.append(cell.text)
                time.sleep(2)
                genel_collection.append(my_elements)
            more_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/table/tbody/tr/td[4]/input')
            driver.execute_script('arguments[0].click();',more_btn)
            time.sleep(2)
        except:
            break
    portfolio_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/ul/li[2]/a')
    driver.execute_script('arguments[0].click();',portfolio_btn)
    time.sleep(2)
    for x in range(2):
        try:
            portfolio_table = driver.find_element_by_css_selector('#MainContent_GridViewDagilim > tbody')
            portfolio_rows = portfolio_table.find_elements_by_tag_name('tr')[1:]
            for row in portfolio_rows:
                my_elements = []
                cells = row.find_elements_by_tag_name('td')
                for cell in cells:
                    my_elements.append(cell.text)
                time.sleep(2)
                portfolio_collection.append(my_elements)
                
            more_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[2]/table/tbody/tr/td[4]/input')
            driver.execute_script('arguments[0].click();',more_btn)
            time.sleep(2)
        except:
            break
    return genel_collection,portfolio_collection



def get_info(start_date,end_date):
    driver.get('https://www.tefas.gov.tr/TarihselVeriler.aspx')
    time.sleep(2)
    btn = driver.find_element_by_css_selector('#MainContent_ButtonSearchDates')
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
    header_text = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody/tr[1]')
    time.sleep(4)
    header_cells = header_text.find_elements_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody/tr[1]/th')
    time.sleep(4)
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
    time.sleep(3)
    genel_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/ul/li[1]/a')
    time.sleep(2)
    driver.execute_script('arguments[0].click();',genel_btn)
    time.sleep(2)
    genel_collection,portfolio_collection = get_rows_text()
    dataframe_holder = []
    for row in genel_collection:
        for adjacent_row in portfolio_collection:
            if (row[0]==adjacent_row[0]) and (row[1]==adjacent_row[1]) and (row[2]==adjacent_row[2]):
                temp = []
                for word in row:
                    temp.append(word)
                for other_words in adjacent_row[3:]:
                    temp.append(other_words)
                dataframe_holder.append(temp)
                genel_collection.remove(row)
                portfolio_collection.remove(adjacent_row)
    print(dataframe_holder)
    df = pd.DataFrame(dataframe_holder,columns=headers)
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
