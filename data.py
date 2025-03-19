from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import time

file = open("datahouse29.csv","w",newline="")
writer=csv.writer(file)           
writer.writerow(['location','bedrooms','bath','size','price'])
for i in range(1,1500):
    
    #html_text = requests.get('https://www.bproperty.com/en/dhaka/properties-for-rent/page-'+str(i)).text  
    html_text = requests.get('https://www.bproperty.com/en/dhaka/properties-for-rent/page-'+str(i)).text 
    
    soup=BeautifulSoup(html_text,'lxml')
    houses = soup.find_all('div', class_='d6e81fd0')
    for house in houses:
        try:
            location = house.find('div', class_ = '_7afabd84').text.replace(' ','')
        except:
            location = ''
        try:
            bedrooms = house.find('span',{'class':'b6a29bc0','aria-label':'Beds'}).text
        except:
            bedrooms = ''
        try:
            bath = house.find('span',{'class':'b6a29bc0','aria-label':'Baths'}).text
        except:
            bath = ''
        try:
            size = house.find('span',{'class':'b6a29bc0','aria-label':'Area'}).text.split()[0].replace(',','')
        except:
            size = ''
        try:
            price= house.find('span', class_ = 'f343d9ce').text.replace(',','')
        except:
            price = ''    
 
        writer.writerow([location,bedrooms,bath,size,price]) 
file.close()
     