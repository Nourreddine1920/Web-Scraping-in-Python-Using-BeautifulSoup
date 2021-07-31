from bs4 import BeautifulSoup
import requests 
#url , request , soup 
url="https://www.udemy.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text , "html.parser")
print(soup.prettify())