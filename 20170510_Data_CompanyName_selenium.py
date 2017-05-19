#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.firefox import firefox_binary
import urllib.parse
import sys

def NamefromGFinance(url): 
    driver = webdriver.firefox
    #driver.get(url)  
    
    div = driver.find_element_by_css_selector('.appbar-snippet-primary')
    company_name = div.text
    print(company_name)
    
    driver.close()
    
if __name__ == '__main__':
    stock = sys.argv[1]
    baseurl = 'https://www.google.com/finance?q='
    url = baseurl + stock
    NamefromGFinance(url)        
    

 
