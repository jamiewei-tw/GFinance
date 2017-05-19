#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#公司簡介加上其他會議資訊並寫入文字檔中

import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

def ProfilefromGFinance(stock, url): 

    head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}   
    response = requests.get(url, headers=head).content
    soup = BeautifulSoup(response, 'lxml')
    Summary = soup.find('div', 'companySummary').contents[0]
    CompanyName = soup.find('div', class_='appbar-snippet-primary').span.text
    WholeTicker = soup.find('div', class_='appbar-snippet-secondary').span.text
    print(WholeTicker)
    content(stock, CompanyName, Summary)

    
    
def content(Stock, CompanyName, Description):
    Company = CompanyName + '(' + Stock + ')'
    W.write("Date & Time: 2017/5/11 AM8:00 Taipei Time\n")
    W.write("Company: " + Company)
    W.write("\n")
    W.write("Spearker: Joan Hoover, IR\n")
    W.write("Language: English\n")
    W.write("Dial In: +886 2 2326 9788\n")
    W.write("Passcode: 8888#\n\n")
    W.write(Description)
    

    
if __name__ == '__main__':
    stock = sys.argv[1]
    Filename = stock + '.txt'
    W = open(Filename, "w")
    baseurl = 'https://www.google.com/finance?q='
    url = baseurl + stock
    ProfilefromGFinance(stock, url)
   
