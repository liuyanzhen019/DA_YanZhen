import requests

url = 'http://172.17.50.43/photography'
r = requests.get(url)
print(r.text)
#This will get the status code
print("Status code:")
print("\n *", r.status_code,"OK")
h = requests.head(url)
#This will only get the headers only
print('Header:\n******')
#To print line by line
for line in h.headers:
    print(line,":",h.headers[line])
print('******')

ur12 = 'http://172.17.50.43/headers.php'
headers = {
    'User-Agent':'Mobile'
}
r2 = requests.get(ur12,headers=headers)
print(r2.text)


