#url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

url = " "

url = url.strip()

if url == "":
    raise ValueError("A URL esta vazia")


indice_interrogacao = url.find("?")
url_base =url[0:indice_interrogacao]


url_parametros= url[indice_interrogacao+1:]
print(url_parametros)

parametros_busca = 'moedaDestino'
indice_parametro =url_parametros.find(parametros_busca)
indice_valor = indice_parametro + len(parametros_busca) + 1
indice_e_comercial = url_parametros.find('&',indice_valor)
if indice_e_comercial ==-1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]


print(valor)