#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

def DescriptionfromGFinance(url):    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    summary = soup.find('div', 'companySummary')
    print(summary.contents[0])
    
if __name__ == '__main__':
    stock = sys.argv[1]
    baseurl = 'https://www.google.com/finance?q='
    url = baseurl + stock
    DescriptionfromGFinance(url)        
    

 
