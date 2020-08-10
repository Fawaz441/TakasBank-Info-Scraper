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
      
        # try:
        # genel_table = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table')
        genel_rows = driver.find_elements_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody/tr')[1:]
        print("genel rows found ",len(genel_rows),' instances')
        for row in genel_rows:
            print('genel row ..............',genel_rows.index(row))
            my_elements = []
            cells = row.find_elements_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody/tr/td')  #issue here
            time.sleep(3)
            for cell in cells:
                my_elements.append(cell.text)
            print('appended texts in cells')
            print(my_elements)
            time.sleep(2)
            genel_collection.append(my_elements)
        more_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/table/tbody/tr/td[4]/input')
        driver.execute_script('arguments[0].click();',more_btn)
        time.sleep(7)
        # except:
        #     print('unale')
        #     pass
    portfolio_btn = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/ul/li[2]/a')
    driver.execute_script('arguments[0].click();',portfolio_btn)
    time.sleep(2)
    for x in range(2):
        try:
            # portfolio_table = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[2]/div[1]/table')
            portfolio_rows = portfolio_table.find_elements_by_tag_name('/html/body/form/div[3]/div[3]/div/div[4]/div[2]/div[1]/table/tbody/tr')[1:]
            print("portfolio_rows  found ",len(portfolio_rows),' instances')
            for row in portfolio_rows:
                print('portfolio row ..............',portfolio_rows.index(row))

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
            print('unale')
            pass
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
    # headers = ['Tarih','Fon Kodu','Fon Adı','Fiyat','Tedavüldeki Pay Sayısı','Kişi Sayısı','Fon Toplam Değer','	Banka Bonosu (%)',
    #             'Diğer (%)','Döviz Ödemeli Bono (%)','Devlet Tahvili (%)','Dövize Ödemeli Tahvil (%)','Eurobonds (%)','Finansman Bonosu (%)	',
    #             'Fon Katılma Belgesi (%)','Gayrı Menkul Sertifikası (%)	','Hazine Bonosu (%)','Hisse Senedi (%)	','Kamu Dış Borçlanma Araçları (%)',
    #             'Katılım Hesabı (%)	','Kamu Kira Sertifikaları (%)','Kıymetli Madenler (%)	','Özel Sektör Kira Sertifikaları (%)','Özel Sektör Tahvili (%)	',
    #             'Repo (%)','Türev Araçları (%)	TPP (%)	','Ters-Repo (%)','Varlığa Dayalı Menkul Kıymetler (%)	','Vadeli Mevduat (%)','Yabancı Borçlanma Aracı (%)	',
    #             'Yabancı Hisse Senedi (%)	','Yabancı Menkul Kıymet (%)']
    headers = []
    time.sleep(5)
    header_text = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody/tr[1]')
    print(header_text)
    time.sleep(3)
    header_cells = header_text.find_elements_by_tag_name('th')
    header_cells = driver.find_elements_by_xpath('/html/body/form/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody/tr[1]/th')
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
    print(len(genel_collection),' instances in genel_collection')
    print(len(portfolio_collection),' instances in portfolio_collection')
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
    print(len(genel_collection),' rows left in genel_collection')
    for left_row in genel_collection:
        helper = []
        for cell in left_row:
            helper.append(cell)
        helper[6:34] = ['-'] * 27
        dataframe_holder.append(helper)

    # Left over rows in the portfolio collection
    print(len(portfolio_collection),' rows left in portfolio_collection')
    for right_row in portfolio_collection:
        helper = []
        for cell in right_row[0:3]:
            helper.append(cell)
        helper[3:7] = ['-'] * 4
        helper[7:34] = right_row[3:]
        dataframe_holder.append(helper)

    df = pd.DataFrame(dataframe_holder,columns=headers)
    df.to_csv(start_date+"  to  "+end_date+'.csv')

    

    



def get_data():
    # Get data to type into input elements on the site.
    print("Enter start date in format DD/MM/YY")
    # start_date = input()
    # start_date = start_date.strip().replace("/",".")
    print("Enter end date in format DD/MM/YY")
    # end_date = input()
    # end_date = end_date.strip().replace("/",".")
    # get_info(start_date,end_date)
    get_info('06.08.2020','06.08.2020')
    
get_data()
