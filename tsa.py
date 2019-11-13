import os
from tkinter import *
print('#######################################################################################################')
os.system('figlet Twitter Sentiment Analyisis')
print('Note:1)Polarity=in sentiment analysis it refers to identifying sentiment orientation (positive, neutral, and negative).')
print('2)Subjectivity= expressions are opinions that describe people’s feelings towards a specific subject or topic.')
print('3)Assisment= Analysis of special word in the tweet.')
print('#######################################################################################################')
os.system('python ui.py > o.txt')
os.system('python test.py > op.txt')
file=open("op.txt","r")
opt=file.read()
try:
    root = Tk()
    root.title('Sentiment Analysis Report')
    T = Text(root, height=200, width=150,font=("arial",12,"bold"),fg="red",bg="white")
    T.pack()
    T.insert(END,opt)
    mainloop()
except TclError:
    os.system('firefox op.txt')
