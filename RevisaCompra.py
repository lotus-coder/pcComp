from bs4 import BeautifulSoup
import requests


class ChekiaGrafica():

    def __init__(self):
        self.url = 'https://www.pccomponentes.com/tarjetas-graficas'
        self.urlotra = 'https://www.pccomponentes.com'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.todasLasPaginas = []
        self.URLS = []
        self.todasLasPaginasValidas = []


    def dameURLs(self,url):
        r = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        lista = soup("article")
        urls = []
        for cosa in lista:
            # print(cosa.prettify(),end='\n\n\n\n')
            for s in cosa("a"):
                if s['href'] not in urls:
                    urls.append(s['href'])
#                print(s['href'],end='\n\n')
        return urls

    def miraURLs(self,listaURLS):
        for url in listaURLS:
            if self.urlotra+url not in  self.URLS:
                self.URLS.append(self.urlotra+url)

    def damePaginasTodas(self,url):
        r = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        lista = soup.find_all("li", class_="c-paginator__next")
        self.todasLasPaginas.append("")
        for link in lista:
            for url in link("a"):
                self.todasLasPaginas.append(url['href'])
        try:
            self.damePaginasTodas(self.url+url['href'])
        except Exception:
            pass

    def esValido(self,url):
        r = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        lista = soup.find("div", {"id": "btnsWishAddBuy"})
        if r.status_code == 200:
            for cosa in lista:
                if "buy-button" in cosa["class"] :
                    return True
                if cosa['id'] == "notify-me":
                    return False

    def trabaja(self):
        self.damePaginasTodas(self.url)
        for cosa in self.todasLasPaginas:
            self.miraURLs(self.dameURLs(self.url+cosa))
        for pagina in self.URLS:
            if self.esValido(pagina):
                self.todasLasPaginasValidas.append(pagina)



if __name__ == "__main__":
    c = ChekiaGrafica()
    c.trabaja()
    c.todasLasPaginasValidas.sort()
    for pagina in c.todasLasPaginasValidas:
        print(pagina)
