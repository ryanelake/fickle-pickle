from tkinter import *
import urllib.request

#Closes the application
def close():
    root.destroy()

#Gets text in the box and prints it (for now)
def update(event=None):
    print(user_in.get())
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
