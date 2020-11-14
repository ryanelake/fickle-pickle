from tkinter import *
import urllib.request
import random
import time
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#Closes the application
def close():
    root.destroy()

#Update the user text box and ai text box
def converse(event=None):
    global emotion
    newUserText = editOutput(user_in.get())
    bot_response = chatbot.get_response(user_in.get())
    newAIText = editOutput(bot_response.text)
    user_out.delete("1.0","end")
    user_out.insert(END, newUserText, "center")
    ai_out.delete("1.0","end")
    ai_out.insert(END, newAIText, "center")
    emotion = random.randint(0,2)
    frame = 0
    front = Label(root, image=animations[emotion][frame], bg="#f3f7d6")
    front.place(x=400,y=0)
    front.lower(ai_out)
    user_in.delete(0,END)

#Make the output strings fit the text boxes
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

#Part of blinking animation
def frame0():
    frame = 0
    front = Label(root, image=animations[emotion][frame], bg="#f3f7d6")
    front.place(x=400,y=0)
    front.lower(ai_out)
    root.after(random.randint(500,3000), frame1)

#Part of blinking animation
def frame1():
    frame = 1
    front = Label(root, image=animations[emotion][frame], bg="#f3f7d6")
    front.place(x=400,y=0)
    front.lower(ai_out)
    root.after(50, frame2)

#Part of blinking animation
def frame2():
    frame = 2
    front = Label(root, image=animations[emotion][frame], bg="#f3f7d6")
    front.place(x=400,y=0)
    front.lower(ai_out)
    root.after(50, frame1Back)

#Part of blinking animation
def frame1Back():
    frame = 1
    front = Label(root, image=animations[emotion][frame], bg="#f3f7d6")
    front.place(x=400,y=0)
    front.lower(ai_out)
    root.after(50, frame0)
    
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

emotion = random.randint(0,2)
frame = 0
back = PhotoImage(file="back.png")
Label(root, image=back, bg="#f3f7d6").place(x=-50,y=200)
animations = [[PhotoImage(file="happy_base.png"), PhotoImage(file="happy_half.png"), PhotoImage(file="happy_close.png")],
         [PhotoImage(file="sad_base.png"), PhotoImage(file="sad_half.png"), PhotoImage(file="sad_close.png")],
         [PhotoImage(file="mad_base.png"), PhotoImage(file="mad_half.png"), PhotoImage(file="mad_close.png")]]
front = Label(root, image=animations[emotion][frame], bg="#f3f7d6")
front.place(x=400,y=0)
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

root.after(0, frame0)

root.mainloop()
