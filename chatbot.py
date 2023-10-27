import openai

API_KEY = "Sua api"

openai.api_key = API_KEY

def enviar_msg(msg, lista_msgs=[]):
  lista_msgs.append(
    {"role": "user", "content": msg}
  )

  resposta = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = lista_msgs,
  )
  return resposta["choices"][0]["message"]

lista_msgs = []
while True:
  texto = input("Escreva aqui a sua mensagem: ")
  if input == "sair":
    break
  else:
    resposta = enviar_msg(texto, lista_msgs)
    lista_msgs.append(resposta)