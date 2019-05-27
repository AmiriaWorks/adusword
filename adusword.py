figlet  -f small admin user wordpress 

import json 

site = input('Enter The Target: ')
ulr = 'https//'+site+'wp-json/wp/v2/user/1'

r = requests.get(url)
y = json.loads(r-text)

print (y['name'])
