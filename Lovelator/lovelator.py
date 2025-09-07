from tkinter import *
import random



def lovelator():

    if name_ent.get() != "" and partner_name_ent.get() != "":
        score_text.set(f"{random.randint(1, 101)}")



if __name__ == "__main__":

    root = Tk()
    root.title("love calculator \u2665")
    root.geometry("300x200")
    root.resizable(height=False, width=False)


    name_lbl = Label(root, text="Your Name:")
    name_lbl.grid(row=0, column=0)

    name_ent = Entry(root, width=20)
    name_ent.grid(row=0, column=1)

    partner_name_lbl = Label(root, text="Partner Name:")
    partner_name_lbl.grid(row=1, column=0)

    partner_name_ent = Entry(root, width=20)
    partner_name_ent.grid(row=1, column=1)


    Button(root, text="\u2665", command=lovelator).grid(row=2, column=1)

    score_text = StringVar()
    love_score = Label(root, textvariable=score_text)
    love_score.grid(row=3, column=1)


    root.mainloop()
    
