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
def update(event=None):
    print("User: ", user_in.get())
    bot_response = chatbot.get_response(user_in.get())
    print("Computer: ", bot_response)
    user_in.delete(0,len(user_in.get()))
    
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/icon.ico", "icon.ico")
root = Tk()
root.title("The Fickle Pickle")
root.geometry('750x500')
root.iconbitmap("icon.ico")
root.configure(bg='blue')

root.bind('<Return>', update)

user_in = Entry(width=100)
user_in.place(x=5,y=475)
temp = Button(text="Enter", width = 7,command=update)
temp.place(x=620,y=470)
temp = Button(text="Quit", width = 6, command=close)
temp.place(x=690,y=470)
           
root.mainloop()
