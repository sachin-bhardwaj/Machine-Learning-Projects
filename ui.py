from tkinter import *
import os 
from PIL import ImageTk, Image
#from PIL import Image

root = Tk()
root.title("Sentiment Analysis")
root.geometry("800x900+0+0")
root.resizable(False, False)

##Heading
heading = Label(root, text = "Twitter Sentiment Analysis ", font = ("Times", 30, "bold italic underline"),bg="black", fg = "red").pack()

label_1 = Label(root, text = "Enter the word to analyse", font = ("Arial Black", 15, "bold"),bg="black", fg = "red").place(x = 90, y = 300)
#label_2 = Label(root,text="Note:- It may take some time for the result to be displayed.",font=("Comic Sans MS",20,"italic"),fg='yellow',bg ='black').place(x=145,y=550)

word = StringVar()
query = StringVar()

entry_1 = Entry(root,textvariable = word,font=("Courier",15,"bold italic"), width = 30, bg = "lightgreen", fg = "black").place(x = 400, y =300)

def do_it():
    query = str(word.get())
    print(query)


submitWord = Button(root, text = "Submit Word",font=("bold"),width = 10, height = 2,bg = "black", fg = "red", command = do_it).place(x = 190, y = 400)
button = Button (root, text = "Show Sentiment Analysis Report",font=("bold"),bg = "black",fg='red',height=2, command = root.destroy).place(x=325,y=400)

path="edit.jpg"

img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img).pack()
label_3 = Label(root,text="Twitter sentiment Project",font=("verdana",15,"bold italic"),fg='#f51deb',bg ='black').pack()
root.configure(background = 'black')
label_4= Label(root, text = "Project by- Sachin Bhardwaj", font = ("Arial Black", 15, "bold"),bg="black", fg = "red").place(x = 50, y = 650)

root.mainloop()
