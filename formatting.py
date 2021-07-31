from bs4 import BeautifulSoup
import requests 
#url , request , soup 
url="https://www.udemy.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text , "html.parser")
#print(soup.find_all('div'))
#print(soup.find_all('style'))
#print(soup.find_all('img'))
#print(soup.find_all('b'))
print(soup.find_all('i'))