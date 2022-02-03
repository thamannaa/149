from tkinter import *
import random
root=Tk()
root.title("random word")
root.geometry("400x400")
root.configure(background="purple")
label=Label(root)

list1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def generate_random_word():
    random_no1=random.randint(0,26)
    random_no2=random.randint(0,26)
    random_no3=random.randint(0,26)
    random_no4=random.randint(0,26)
    random_no5=random.randint(0,26)
    
    random_letter1=list1[random_no1]
    random_letter2=list1[random_no2]
    random_letter3=list1[random_no3]
    random_letter4=list1[random_no4]
    random_letter5=list1[random_no5]
    
    label["text"]=random_letter1+random_letter2+random_letter3+random_letter4+random_letter5
    


btn=Button(root,text="generate a romdom word",command=generate_random_word,bg="Royal Blue",fg="White")
label.place(relx=0.5,rely=0.4,anchor=CENTER)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()


