import requests
url = "https://httpbin.org/ip"
proxy = {'https':'http://191.235.98.23:3128'}
r = requests.get(url,proxies=proxy)
print(r.status_code)
r = r.json()
print(r["origin"])