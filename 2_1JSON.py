import requests

url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

r = requests.get(url)

json_data =r.json()

for k in json_data.keys():
    print(k,':',json_data[k])

# for k,v in json_data.items():
#     print(k,':',v)
#
# print(r.text)
