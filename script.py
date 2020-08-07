import time
import requests
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
from bs4 import BeautifulSoup
executable_path = r'C:\Users\user\Desktop\Fawaz\chromedriver.exe'
chrome_options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(executable_path=executable_path)

def get_info(start_date,end_date):
    url = 'https://www.tefas.gov.tr/TarihselVeriler.aspx'
    driver.get('https://www.tefas.gov.tr/TarihselVeriler.aspx')
    btn = driver.find_element_by_css_selector('#MainContent_ButtonSearchDates')
    btn.click()
    time.sleep(12)
    stuff = requests.get(url)
    data = {'ctl00$MainContent$TextBoxStartDate':start_date,'ctl00$MainContent$TextBoxEndDate':end_date,'_form_action':'Save'}
    
    p = requests.post(url,data)
    soup = BeautifulSoup(p.text,'html.parser')
    listed = soendup.find('table','fund-grid')
    rows = listed.find_all('tr')[1:]
    headers_ = []
    headers = soup.find('tr','fund-grid-header')
    temp = headers.find_all('th')
    for th in temp:
        headers_.append(th.text)
    print(headers_)


    
    all_data = []
    for row in rows:
        content = row.contents
        content = list(filter(('\n').__ne__, content))
        content = list(filter(('\r\n').__ne__, content))
        new_content = []
        for stuff in content:
            new_content.append(stuff.string.strip())
            # new_content = list(filter(('\n').__ne__, new_content))
            # new_content = list(filter(('\r\n').__ne__, new_content))
        all_data.append(new_content)
  
    df = pd.DataFrame(all_data,columns=headers_)
    df.to_csv('test.csv')

def get_data():
    print("Enter start date in format DD/MM/YY")
    start_date = input()
    start_date = start_date.strip().replace("/",".")
    print("Enter end date in format DD/MM/YY")
    end_date = input()
    end_date = end_date.strip().replace("/",".")
    get_info(start_date,end_date)
    

get_data()
