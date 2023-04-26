import requests

url = 'https://api.agify.io/?name=jin'

print(requests.get(url).json())

#requests.get('https://api.agify.io/?name=jin')

#requests.get('https://api.agify.io/?name=jin').json()


# $ pip install requests 콘솔에 하기