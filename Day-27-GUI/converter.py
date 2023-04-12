import tkinter
import sys

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

my_input = tkinter.Entry(width=10)
my_input.grid(column=1, row=0)

label_mile = tkinter.Label(text="Miles")
label_mile.grid(column=2, row=0)

label1 = tkinter.Label(text="is equal to")
label1.grid(row=1, column = 0)

label2 = tkinter.Label(text="")
label2.grid(row=1, column = 1)

label3 = tkinter.Label(text="Km")
label3.grid(row=1, column = 2)


def button_clicked():
    miles = float(my_input.get())
    km = miles * 1.609
    label2["text"] = float(km)


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

def close(event):
    sys.exit()

window.bind('<Escape>',close)

while True:
    window.mainloop()