BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
from tkinter import *
from tkinter import messagebox
import random
current_card={}
to_learn={}

#ÖĞRENİLMEMİŞ OLANLARI OKUMAYA ÇALIŞ 
try:
    data=pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv("language.csv")
    print(original_data)
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
    
        
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card =random.choice(to_learn)
    canvas.itemconfig(card_title,text="Italian")
    canvas.itemconfig(card_text,text=current_card["Italian"])
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer=window.after(3000,func=flip_card)

    


def flip_card():
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_text,text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)
    
def is_known():
    to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv",index=False)
    
    next_card()
    
    
##KULLANICI ARAYÜZÜ
window=Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)



canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file="card_front.png")
card_back_img=PhotoImage(file="card_back.png")

card_background=canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_text=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)



cross_image=PhotoImage(file="wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image=PhotoImage(file="right.png")
known_button=Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()