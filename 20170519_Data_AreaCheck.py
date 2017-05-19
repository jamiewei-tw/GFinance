#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#辨別股票國家別

import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

def ProfilefromGFinance(ticker, url): 

    head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}   
    response = requests.get(url, headers=head).content
    soup = BeautifulSoup(response, 'lxml')
    Summary = soup.find('div', 'companySummary').contents[0]
    CompanyName = soup.find('div', class_='appbar-snippet-primary').span.text
    WholeTicker = soup.find('div', class_='appbar-snippet-secondary').span.text
    
    R_ticker = '(' + ticker + areacheck(WholeTicker) + ')'
    content(R_ticker, CompanyName, Summary)

def areacheck(Ticker):
    Area = ''
    location = Ticker.find(':')
    area = Ticker[1:location]
    US = ['NASDAQ','NYSE','AMEX']
    CH = ['SHE','SHA']
    
    
    if (area in US):
        Area = ' US'
        
    elif (area in CH):
        Area = ' CH'
        
    elif area == 'HKG':
        Area = ' HK'
        
    elif area == 'TYO':
        Area = ' JP'
        
    else:
        Area = ''
     
    return Area
    
    
    
def content(Stock, CompanyName, Description):
    Company = CompanyName + Stock 
    W.write("Date & Time: 2017/5/11 AM8:00 Taipei Time\n")
    W.write("Company: " + Company)
    W.write("\n")
    W.write("Spearker: Joan Hoover, IR\n")
    W.write("Language: English\n")
    W.write("Dial In: +886 2 2326 9788\n")
    W.write("Passcode: 8888#\n\n")
    W.write(Description)
    

    
if __name__ == '__main__':
    ticker = sys.argv[1]
    Filename = ticker + '.txt'
    W = open(ticker, "w")
    baseurl = 'https://www.google.com/finance?q='
    url = baseurl + ticker
    ProfilefromGFinance(ticker, url)
   
