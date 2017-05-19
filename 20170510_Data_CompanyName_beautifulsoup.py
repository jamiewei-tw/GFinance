#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

def CompanyNamefromGFinance(url):  
    head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}  
    response = requests.get(url, headers=head).content
    soup = BeautifulSoup(response, 'lxml')
    Name = soup.find('div', class_='appbar-snippet-primary')
    print(Name.span.text)
    
if __name__ == '__main__':
    stock = sys.argv[1]
    baseurl = 'https://www.google.com/finance?q='
    url = baseurl + stock
    CompanyNamefromGFinance(url)        
    

 
