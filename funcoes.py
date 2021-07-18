import requests
from bs4 import BeautifulSoup


# 1 - COLOCA O CODIGO DE RASTREIO NO ID DA
def personaliza_url(codigo_rastreio):
  url_personalizada=f'https://www.linkcorreios.com.br/?id={codigo_rastreio}'
  return url_personalizada



def testa_url_pega_texto(url):
  try:
    requisicao=requests.get(url)
    if requisicao.status_code==200:
      print('Conseguimos acessar: ')
      print(url)
      html_texto=requisicao.text
      return html_texto
    else:
      print(f'Código retornado: {requisicao.status_code}')
  except:
    print('Não foi possível acessar a requisição')




def sopa_de_letras_pega_status(html_texto):
  soup=BeautifulSoup(html_texto,'html.parser')
  try:
    tag_resultado=soup.find('b').get_text()
  except:
    tag_resultado="Não existe código de rastreio para este objeto"
  
  return tag_resultado


