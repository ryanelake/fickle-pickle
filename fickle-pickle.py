from tkinter import *
import urllib.request

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
        "Ron",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.BestMatch'
        ],
        database_uri='sqlite:///database.db'
        )

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

#Closes the application
def close():
    root.destroy()

#Gets text in the box and prints it (for now)
def converse(event=None):
    user_out.delete("1.0","end")
    user_out.insert(END, user_in.get())
    bot_response = chatbot.get_response(user_in.get())
    print("Computer: ", bot_response)
    user_in.delete(0,len(user_in.get()))
    
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/icon.ico", "icon.ico")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/back_pickle.png", "back.png")
root = Tk()
root.title("The Fickle Pickle")
root.geometry('500x500')
root.iconbitmap("icon.ico")
root.configure(bg='#f3f7d6')
root.bind('<Return>', converse)

image = PhotoImage(file="back.png")
Label(root, image=image, bg="#f3f7d6").place(x=-50,y=200)
user_in = Entry(width=58)
user_in.place(x=5,y=475)
temp = Button(text="Enter", width = 7,command=converse)
temp.place(x=370,y=470)
temp = Button(text="Quit", width = 6, command=close)
temp.place(x=440,y=470)
user_out = Text(root, height=5, width = 19, bd=0)
user_out.place(x=195,y=260)
           
root.mainloop()
