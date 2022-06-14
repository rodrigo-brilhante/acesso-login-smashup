import sys
import requests
import time
from requests.structures import CaseInsensitiveDict

class SmashupDouble():
	def run(self):
		with requests.Session() as session:
			session.post("https://player.smashup.com/iframe_module/iframe_login", data="login=gui2400&password=SJzFnMLesI1&remember_me=on&act=iframe_login")
			period_anterior=''
			while True:
				try:
					headers = CaseInsensitiveDict()
					headers["x-auth-key"] = "daX5ehgs5OGpZQyZFVbBIb"
					r=session.get('https://br-game-api.t1tcp.com/mini/double/opencodes?&pagesize=15&page=1', headers=headers)

					period=r.json()['items'][0]['period']
					number=r.json()['items'][0]['number']
					color=r.json()['items'][0]['color']

					if period != period_anterior:
						print("numero: ", number)
						print("cor: ", color)
					period_anterior=period
					time.sleep(2)
				except:
					pass

sm = SmashupDouble()
sm.run()