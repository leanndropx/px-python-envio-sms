import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from flask import render_template, request, Flask
import funcoes


app=Flask('EnvioSMS')

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/enviado')
def enviado():
  rastreio=request.args.get('codigorastreio')
  telefone=request.args.get('telefone')

  url_personalizada=funcoes.personaliza_url(rastreio)
  html_texto=funcoes.testa_url_pega_texto(url_personalizada)
  texto_status=funcoes.sopa_de_letras_pega_status(html_texto)
  
  #envia sms
  account_sid = 'ACabc9503cb7e4f757e193b2b2b77ad2bf'
  auth_token = 'c274b6cc7be4668a69cf332cb6a710fe'
  client = Client(account_sid, auth_token)

  client.messages.create(
    to=f'+55{telefone}',
    from_='++15732084369',
    body=f'Status do seu pedido: {texto_status}')

  return render_template('enviado.html',rastreio=rastreio,telefone=telefone, status=texto_status)

app.run('0.0.0.0')


