import requests

form_data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=form_data)
print(response.text)
