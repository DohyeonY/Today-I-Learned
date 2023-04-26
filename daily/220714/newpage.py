import requests
from bs4 import BeautifulSoup

url = 'http://finance.naver.com/sise/'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
kospi = data.select_one('#KOSPI_now')
result = kospi.text

print(result)