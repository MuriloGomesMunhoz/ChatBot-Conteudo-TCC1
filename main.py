import tkinter as tk
from tkinter import scrolledtext
from chatbot import ChatBot
from tkinter import *


myChatBot = ChatBot()
myChatBot.loadModel()

# myChatBot.createModel()

root = tk.Tk()
root.attributes('-zoomed', True)
root.title("ChatBot")

chat_log = scrolledtext.ScrolledText(root, width=30, height=10, font='Arial', bg="#e6e6e6")
chat_log.insert(tk.END, "Bem Vindo(a) a aula de TCC 1\n\n")
chat_log.insert(tk.END, "Digite sua dúvida\n\n")
chat_log.pack(fill='both', expand=True)

input_field = tk.Entry(root, bd=1, font=('Arial', 20),bg="#e6e6e6", highlightbackground="Black", width=500)
input_field.pack()

chat_log.tag_configure("user", foreground="#442265", font=("Verdana", 12))

def send_message(event):
    # Obtém a mensagem digitada pelo usuário
    msg = input_field.get()
    if msg != '':
        # Exibe a mensagem do usuário no chat
        chat_log.config(state=NORMAL)
        chat_log.insert(tk.END, "Você: " + msg + '\n\n', "user")
        chat_log.config(state=DISABLED)

        # Obtém a resposta do chatbot e exibe no chatf
        res = myChatBot.chatbot_response(msg)
        chat_log.config(state=NORMAL)
        chat_log.tag_config("message", font=("Verdana", 12))
        chat_log.insert(tk.END, "Você: " + res + '\n\n', "message")
        chat_log.config(state=DISABLED)
        chat_log.yview(END)

        # Limpa a caixa de entrada de texto
        input_field.delete(0, tk.END)

input_field.bind("<Return>", send_message)

root.mainloop()
