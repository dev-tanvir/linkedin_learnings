import requests

url = 'https://jsonplaceholder.typicode.com/photos'

response = requests.get(url)
url_list = []
print(response.json())

for element in response.json():
    # print(element)
    url_list.append(element['url'])

if len(url_list) != len(set(url_list)):
    print('Contents have duplicate urls')
else:
    print(len(url_list))
    print(len(set(url_list)))
    print("No duplicate urls")

