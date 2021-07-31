from bs4 import BeautifulSoup
import requests 
import csv 
#url , request , soup 
url="https://www.udemy.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text , "html.parser")
print(soup.title)
file = csv.writer(open("output.csv" , "w"))
file.writerow([soup.title])

