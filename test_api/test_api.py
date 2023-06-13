import requests

HOST = 'http://127.0.0.1:8000'
res = requests.post(HOST + '/api-token-auth/', {
    'username':'abc',
    'password':'khu12345',
})

res.raise_for_status()
token = res.json()['token']
print(token)

headers = {'Authorization': 'JWT' + token, 'Accept' : 'application/json'}

data = {
    'title' : '이미지 03',
    'text' : 'API 내용',
    'created_date' : '2023-06-12T19:28:00+09:00',
    'published_date' : '2023-06-12T19:28:00+09:00'
}
file={'image' : open('/Users/juhyu/Desktop/4-1/모바일웹프로그래밍/과제12/맹구.webp', 'rb')}
res = requests.post(HOST + '/api_root/Post/', data=data, files=file, headers=headers)
print(res)
print(res.json())