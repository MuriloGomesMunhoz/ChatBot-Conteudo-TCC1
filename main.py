from chatbot import ChatBot
myChatBot = ChatBot()
print("(1) para criar o modelo")
Aux = int(input("(0) para carregar o modelo"))

if(Aux == 1):
    # apenas carregar um modelo pronto
    myChatBot.loadModel()
elif(Aux == 0):
    # criar o modelo
    myChatBot.createModel()


print("Bem vindo a aula de TCC 1")

pergunta = input("Como posso te ajudar?")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="despedida"):
    pergunta = input("posso lhe ajudar com algo a mais?")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")


print("Foi um prazer atendê-lo")
