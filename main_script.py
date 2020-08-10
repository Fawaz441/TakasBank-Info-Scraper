import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
chrome_options = Options()
# executable_path = r'C:\Users\Fawaz\Desktop\Dowstrademus\chromedriver.exe'
executable_path = r'C:\Users\user\Desktop\Fawaz\chromedriver.exe'
chrome_options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(executable_path=executable_path)


def get_rows_text():
    genel_collection = []
    portfolio_collection = []
    for c in range(2):
        try:
            genel_rows = driver.find_elements_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody/tr')[1:]
            time.sleep(8)
            print("genel rows found ",len(genel_rows),' instances')
            for row in genel_rows:
                innerHTML = row.get_attribute('innerHTML')
                time.sleep(4)
                print('genel row ..............',genel_rows.index(row))
                my_elements = []
                soup3 = BeautifulSoup(innerHTML,'html.parser')
                cells = soup3.find_all('td')  
                for cell in cells:
                    my_elements.append(cell.text.replace('\n','').lstrip().rstrip())
                time.sleep(2)
                genel_collection.append(my_elements)
            more_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/table/tbody/tr/td[4]/input')
            driver.execute_script('arguments[0].click();',more_btn)
            time.sleep(7)
        except:
            print('unable to complete the process')
            break

    # Getting portfolio info
    portfolio_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/ul/li[2]/a')
    driver.execute_script('arguments[0].click();',portfolio_btn)
    time.sleep(2)
    for x in range(2):
        try:
            portfolio_rows = driver.find_elements_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[2]/div[1]/table/tbody/tr')[1:]
            time.sleep(8)
            print("portfolio_rows  found ",len(portfolio_rows),' instances')
            for row in portfolio_rows:
                innerHTML = row.get_attribute("innerHTML")
                time.sleep(6)
                print('portfolio row ..............',portfolio_rows.index(row))
                my_elements = []
                soup4 = BeautifulSoup(innerHTML,'html.parser')
                cells = soup4.find_all('td')
                for cell in cells:
                    my_elements.append(cell.text.replace('\n','').lstrip().rstrip())
                time.sleep(2)
                portfolio_collection.append(my_elements)
            more_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[2]/table/tbody/tr/td[4]/input')
            driver.execute_script('arguments[0].click();',more_btn)
            time.sleep(7)
        except:
            print('unable to complete the process..')
            break
    return genel_collection,portfolio_collection



def get_info(start_date,end_date):
    # Get the info on the site
    driver.get('https://www.tefas.gov.tr/TarihselVeriler.aspx')
    time.sleep(2)
    btn = driver.find_element_by_css_selector('#MainContent_ButtonSearchDates') #orange button to click after inputting dates
    time.sleep(4)
    input_box_one = driver.find_element_by_css_selector('#MainContent_TextBoxStartDate') #start date input element
    input_box_two = driver.find_element_by_css_selector('#MainContent_TextBoxEndDate') #end date input element
    input_box_one.clear()
    input_box_one.send_keys(start_date)
    input_box_two.clear()
    input_box_two.send_keys(end_date)
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(20)

    headers = []
    header_text = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody/tr[1]')
    time.sleep(5)
    header_text = header_text.get_attribute('innerHTML')
    time.sleep(4)
    soup = BeautifulSoup(header_text,'html.parser')
    header_cells = soup.find_all('th')
    for header_cell in header_cells:
        headers.append(header_cell.text)
    time.sleep(5)

#   Gotten headers from general 
#   click portfolio button
    portfolio_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/ul/li[2]/a')
    driver.execute_script("arguments[0].click();", portfolio_btn)
    time.sleep(5)

    #getting portfolio headers...
    other_headers = driver.find_element_by_xpath('//*[@id="MainContent_GridViewDagilim"]/tbody/tr[1]')
    time.sleep(5)
    other_headers = other_headers.get_attribute('innerHTML')
    time.sleep(2)
    soup2 = BeautifulSoup(other_headers,'html.parser')
    other_header_cells = soup2.find_all('th')[3:]
    for header in other_header_cells:
        headers.append(header.text)
    time.sleep(3)
    # click genel btn to go back
    genel_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/ul/li[1]/a')
    time.sleep(2)
    driver.execute_script('arguments[0].click();',genel_btn)
    genel_collection,portfolio_collection = get_rows_text()
    file_opener = open('check.txt','w',encoding="utf-8")
    file_opener.write(str(genel_collection[0]))
    file_opener.write(str(portfolio_collection[0]))
    file_opener.close()
    print(len(genel_collection),' instances in genel_collection')
    print(len(portfolio_collection),' instances in portfolio_collection')
    dataframe_holder = []
    for row in genel_collection:
        for adjacent_row in portfolio_collection:
            if (row[0] in adjacent_row[0]) and (row[1] in adjacent_row[1]):
                temp = []
                for word in row:
                    temp.append(word)
                for other_words in adjacent_row[3:]:
                    temp.append(other_words)
                dataframe_holder.append(temp)
                genel_collection.remove(row)
                portfolio_collection.remove(adjacent_row)
    print(len(genel_collection),' rows left in genel_collection')
    for left_row in genel_collection:
        helper = []
        for cell in left_row:
            helper.append(cell)
        helper[7:34] = ['-'] * 26
        print(len(helper))
        dataframe_holder.append(helper)

    # Left over rows in the portfolio collection
    print(len(portfolio_collection),' rows left in portfolio_collection')
    for right_row in portfolio_collection:
        helper = []
        for cell in right_row[0:3]:
            helper.append(cell)
        helper[3:7] = ['-'] * 4
        helper[7:34] = right_row[3:]
        print(len(helper))
        dataframe_holder.append(helper)

    df = pd.DataFrame(dataframe_holder,columns=headers)
    df.to_csv(start_date+"  to  "+end_date+'.csv')

    

    



def get_data():
    # Get data to type into input elements on the site.
    print("Enter start date in format DD/MM/YYYY")
    start_date = input()
    start_date = start_date.strip().replace("/",".")
    print("Enter end date in format DD/MM/YYYY")
    end_date = input()
    end_date = end_date.strip().replace("/",".")
    get_info(start_date,end_date)
get_data()
