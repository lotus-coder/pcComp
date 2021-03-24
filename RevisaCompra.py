from bs4 import BeautifulSoup
import requests



class ChekiaGrafica():
    url = 'https://www.pccomponentes.com/tarjetas-graficas'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    def dameURLs(self,soup):
        lista = soup("article")
        urls = []
        for cosa in lista:
            # print(cosa.prettify(),end='\n\n\n\n')
            for s in cosa("a"):
                urls.append(s['href'])
                print(s['href'],end='\n\n')
        return urls
