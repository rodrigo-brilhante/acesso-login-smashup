import sys
from bs4 import BeautifulSoup
import requests
import time
from requests.structures import CaseInsensitiveDict

class SmashupFutbol():
    def run(self):
        with requests.Session() as session:
            session.post("https://player.smashup.com/iframe_module/iframe_login", data="login=gui2400&password=SJzFnMLesI1&remember_me=on&act=iframe_login")
            lista_anterior=''
            while True:
                try:
                    # headers = CaseInsensitiveDict()
                    # headers["x-auth-key"] = "daX5ehgs5OGpZQyZFVbBIb"
                    # resp=session.get('https://player.smashup.com/player_center/goto_common_game/5941/1000000?_ga=2.266187277.367080804.1654517135-1455606098.1654290077', headers=headers)
                    resp=session.get('https://player.smashup.com/player_center/goto_common_game/5941/1000000?_ga=2.266187277.367080804.1654517135-1455606098.1654290077')
                    
                    soup = BeautifulSoup(resp.text, 'html.parser')
                    print(resp.text)

                    # resultados = soup.find_all('div', {"class":"History--09963"})

                    # print(soup)
                    sys.exit()
                    if lista_atual != lista_anterior:
                        print("resultado: ", point)
                        period_anterior=period
                    time.sleep(2)
                except:
                    sys.exit()

                    pass

sm = SmashupFutbol()
sm.run()