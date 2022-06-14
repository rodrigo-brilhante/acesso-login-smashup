import sys
import requests
import time
from requests.structures import CaseInsensitiveDict

class SmashupCrash():
	def run(self):
		with requests.Session() as session:
			session.post("https://player.smashup.com/iframe_module/iframe_login", data="login=gui2400&password=SJzFnMLesI1&remember_me=on&act=iframe_login")
			period_anterior=''
			while True:
				try:
					headers = CaseInsensitiveDict()
					headers["x-auth-key"] = "daX5ehgs5OGpZQyZFVbBIb"
					r=session.get('https://br-game-api.t1tcp.com/mini/crash/opencodes?&pagesize=15&page=1', headers=headers)

					period=r.json()['items'][0]['period']
					point=r.json()['items'][0]['point']

					if period != period_anterior:
						print("resultado: ", point)
					period_anterior=period
					time.sleep(2)
				except:
					pass

sm = SmashupCrash()
sm.run()