import requests

query = 'banana'
api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
response = requests.get(api_url, headers={'X-Api-Key': 'HKiH5ZTgzjsCrA+QnCvkkQ==4xOj4GY24Aj7D8mU'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)