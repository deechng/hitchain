import requests

user_info = {'name': 'Bitcoin,Ethereum,XRP,EOS,Bitcoin Cash,Stellar,IOTA'}
r = requests.post("http://localhost/coin/api/id", data=user_info)
print(r.text)