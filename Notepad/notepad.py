from tkinter import *
from tkinter import filedialog



def save_file():
    file_name = filedialog.asksaveasfilename(parent=root)

    with open(file_name, 'w') as fout:
        fout.write(text.get('1.0', END))

def open_file():
    text.delete('1.0', END)

    file_name = filedialog.askopenfilename(parent=root)
    if file_name:
        with open(file_name, 'r') as fin:
            data = fin.read()
            text.insert(END, data)



root = Tk()
root.title('notepad')


text = Text(root, font=('Tahoma', 20))
text.pack(expand=True, fill=BOTH)

footer_label = Label(text="UTF-8")
footer_label.pack()


menu = Menu(root)
menu.add_command(label='save', command=save_file)
menu.add_command(label='open', command=open_file)
menu.add_command(label='exit', command=root.quit)
root.config(menu=menu)



root.mainloop()