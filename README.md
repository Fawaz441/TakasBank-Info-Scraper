# TakasBank-Info-Scraper
A script to scrape data from https://www.tefas.gov.tr/TarihselVeriler.aspx

This script was used to scrape data from the web page listed above. It takes in a start date and end date
The website contains financial data about Securities Mutual Funds, Exchange Traded Funds and Pension Funds

- The scraper utilizes selenium because of the nature of the site (it is Javascript Heavy)
- It also uses Beautiful Soup, a useful python tool for examining and parsing html content.
- The website uses Jquery to make XHR requests to get data.
- The required data is obtained and arranged into lists and dictionaries
- After obtaining all the data, it is exported into a csv file with pandas
