from urllib import response
import requests

url = 'https://api.agify.io/?name=jin'
response = requests.get(url).json()
print(response)
print(response.get('name'))

print(response.get('age'))


#KOSPI_now