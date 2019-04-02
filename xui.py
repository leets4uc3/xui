import requests
#by PHOSPHENE
r = requests.post('https://b.utair.ru/api/v1/login/',
   data = {'login':'380506497153'},
   headers = {
   'Accept-Language':'en-US,en;q=0.5',
   'Connection':'keep-alive',
   'Host':'b.utair.ru',
   'origin':'https://www.utair.ru',
   'Referer':'https://www.utair.ru/'})
#by PHOSPHENE
print(r)
print(r.text)
