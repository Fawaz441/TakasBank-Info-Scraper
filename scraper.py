import requests
import pandas as pd


class Scraper:
    '''Scraper'''
    start_date = None
    end_date = None

    def get_dates(self):
        '''method to take in date inputs from the user'''
        print("Enter start date in format DD/MM/YYYY")
        start_date = input()
        self.start_date = start_date.strip().replace("/",".")
        print("Enter end date in format DD/MM/YYYY")
        end_date = input()
        self.end_date = end_date.strip().replace("/",".")

    def get_data(self):
        '''This is the method that makes the API call'''
        url = "https://www.tefas.gov.tr/api/DB/BindHistoryInfo"
        data = {
            "fontip":"YAT",
            "sfontur":"",
            "fonkod":"",
            "fongrup":"",
            "bastarih":self.start_date,
            "bittarih":self.end_date,
            "fonturkod":"",
            "fonunvantip":""
        }
        response = requests.post(url, json=data,timeout=30)
        return response.json()

    def run(self):
        '''This is the method that runs the previous methods sequentially'''
        self.get_dates()
        print("Processing.............")
        data = self.get_data().get("data")
        df = pd.DataFrame(data,columns=list(data[0].keys()))
        df.to_csv(self.start_date+"  to  "+self.end_date+'.csv')


scraper = Scraper()
scraper.run()
