url=' https://login.ionos.fr/'

import requests

with requests.Session() as s:
	url = ' https://login.ionos.fr/'
	s.get(url)
	login_data= {'oaologin.username: test': fv}