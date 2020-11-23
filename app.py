from win10toast import ToastNotifier
import time
import requests
import json

last_value = 0

def save_json(json_value):
  from datetime import datetime
  now = datetime.now()
  dt_string = now.strftime("%Y%m%d%H%M%S")
  with open(f".\data\EUR-BLR-{dt_string}.json", 'w') as json_file:
    json.dump(json_value, json_file)

def executeRequest():
  global last_value

  response = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')

  json_response = response.json()
  repository = json_response['EUR']
  current = repository['ask']
  
  save_json(json_response)

  message = f"Valor Anterior: {last_value}, Valor Atual: {current}, Variacao: {repository['pctChange']}"
  print(f"{time.ctime()} - {message}")
  toaster = ToastNotifier()
  toaster.show_toast("EURO Value now", message)
     
  last_value = current
  time.sleep(40)


while True:
  executeRequest()