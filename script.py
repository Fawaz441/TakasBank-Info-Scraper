import time
import requests
from bs4 import BeautifulSoup

def get_info():
    url = 'https://www.tefas.gov.tr/TarihselVeriler.aspx'
    stuff = requests.get(url)
    # data = {'ctl00$MainContent$TextBoxStartDate':start_date,'ctl00$MainContent$TextBoxEndDate':end_date,'_form_action':'Save'}
    # p = requests.post(url,data)
    soup = BeautifulSoup(stuff.text,'html.parser')
    soup.prettify()
    listed = soup.find('table','fund-grid')
    rows = listed.find_all('tr')
    # for stuff in listed.children:
    #     print(stuff.string)




# def tickers_info():
#     rows = driver.find_elements_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody')
#     print(rows)
#     for row in rows:
#         print(row.text)






def get_data():
    print("Enter start date in format DD/MM/YY")
    start_date = input()
    start_date = start_date.strip().replace("/",".")
    print(start_date)
    print("Enter end date in format DD/MM/YY")
    end_date = input()
    end_date = end_date.strip().replace("/",".")
    print(end_date)
    get_info(start_date,end_date)
    

get_info()
