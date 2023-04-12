import tkinter
import sys

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

#! LABEL
my_label = tkinter.Label(text="My label", font=("Arial", 24, "bold"))
my_label.config(padx=100, pady=200)
my_label.grid(column=0, row=0)

my_label["text"] = "New text"

#! BUTTON

def button_clicked():
    print('I got clicked')
    my_label["text"] = my_input.get()


button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


button2 = tkinter.Button(text="New button")
button2.grid(column=2, row=0)
#Entry

my_input = tkinter.Entry(width=10)
my_input.grid(column=3, row=2)

def close(event):
    sys.exit()

window.bind('<Escape>',close)

while True:
    window.mainloop()