#!/usr/bin/python3
# -*- coding: UTF-8 -*-


#將公司簡介寫入txt文字檔中

import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

def DescriptionfromGFinance(url):    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    summary = soup.find('div', 'companySummary')
    #print(summary.contents[0])
    return summary.contents[0]
    
if __name__ == '__main__':
    stock = sys.argv[1]
    Filename = stock + '.txt'
    W = open(Filename, "a")
    baseurl = 'https://www.google.com/finance?q='
    url = baseurl + stock
    W.write(DescriptionfromGFinance(url))   
    

 
