class ExtratorURL:
    def __init__(self,url):
        self.url =self.sanitiza_url(url)

    def sanitiza_url(self, url):
        return url.strip()


extator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = extator_url.get_valor_parametro("")