class ExtratorURL:
    def __init__(self,url):
        self.url =self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_paramentros = self.url[indice_interrogacao+1:]
        return url_paramentros

    def get_valor_parametro(self, parametros_busca):
        indice_parametro = self.get_url_parametros().find(parametros_busca)
        indice_valor = indice_parametro + len(parametros_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor






extator_url = ExtratorURL(None)
valor_quantidade = extator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
