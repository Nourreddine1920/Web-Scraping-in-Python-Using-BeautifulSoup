from bs4 import BeautifulSoup
import requests 
import csv
#url , request , soup 
url="https://www.udemy.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text , "html.parser")
for link in soup.find_all('a') : 
    print(link.get('href'))

file = csv.writer(open("output.csv" , "w"))
file.writerow([soup.find_all('a')])



