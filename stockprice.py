import requests
from bs4 import BeautifulSoup
def parseprice() : 
    req = requests.get('https://in.finance.yahoo.com/quote/%5EBSESN?p=%5EBSESN')
    soup = BeautifulSoup(req.text , 'lxml')
    price = soup.find('div ' , {'class' : 'D(ib) Mend(20px)'}).findAll('span')
    return price[0].text
while True : 
    print('the current price : ' +str(parseprice()))