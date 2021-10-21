import requests
import json
from secrets import API_KEY

url = 'https://dunwoody.instructure.com/api/v1/courses?per_page=50'
bearer = 'Bearer ' + API_KEY
headers = {'Authorization': bearer}
response = requests.get(url, headers=headers)
print('My courses:')
data = json.loads(response.content)
for course in data:
    print(course['name'])
