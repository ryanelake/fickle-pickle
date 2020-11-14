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

#18 characters
def converse(event=None):
    newUserText = editOutput(user_in.get())
    bot_response = chatbot.get_response(user_in.get())
    newAIText = editOutput(bot_response.text)
    user_in.delete(0,END)
    user_out.delete("1.0","end")
    user_out.insert(END, newUserText, "center")
    ai_out.delete("1.0","end")
    ai_out.insert(END, newAIText, "center")

def editOutput(output):
    toEdit = output[:]
    toReturn = ""
    temp = ""
    for i in range(len(output)):
        if output[i] == " ":
            toEdit = toEdit[1:]
            if len(temp) + len(toEdit[0:toEdit.find(" ")]) > 18:
                toReturn += temp + "\n"
                temp = ""
            else:
                temp += " "
        else:
            temp += output[i]
            toEdit = toEdit[1:]
    toReturn += temp
    return toReturn
                
            
    
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/icon.ico", "icon.ico")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/back_pickle.png", "back.png")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/Happy.png", "happy_base.png")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/Happy_ClosedEyes.png", "happy_close.png")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/Happy_HalfClosedEyes.png", "happy_half.png")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/Mad.png", "mad_base.png")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/Mad_ClosedEyes.png", "mad_close.png")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/Mad_HalfClosedEyes.png", "mad_half.png")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/Sad.png", "sad_base.png")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/Sad_ClosedEyes.png", "sad_close.png")
urllib.request.urlretrieve("https://raw.githubusercontent.com/ryanelake/fickle-pickle/main/Sad_HalfClosedEyes.png", "sad_half.png")

root = Tk()
root.title("The Fickle Pickle")
root.geometry('830x500')
root.iconbitmap("icon.ico")
root.configure(bg='#f3f7d6')
root.bind('<Return>', converse)

back = PhotoImage(file="back.png")
Label(root, image=back, bg="#f3f7d6").place(x=-50,y=200)
front = PhotoImage(file="happy_half.png")
Label(root, image=front, bg="#f3f7d6").place(x=400,y=0)
user_in = Entry(width=58)
user_in.place(x=5,y=475)
temp = Button(text="Enter", width = 7,command=converse)
temp.place(x=370,y=470)
temp = Button(text="Quit", width = 6, command=close)
temp.place(x=440,y=470)
user_out = Text(root, height=5, width = 19, bd=0)
user_out.tag_configure("center",justify='center')
user_out.place(x=195,y=260)
ai_out = Text(root, height=5, width = 19, bd=0)
ai_out.tag_configure("center",justify='center')
ai_out.place(x=450,y=20)
           
root.mainloop()
