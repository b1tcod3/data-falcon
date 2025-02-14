import requests

response = requests.get('https://oxylabs.io/')
print(response.text)
