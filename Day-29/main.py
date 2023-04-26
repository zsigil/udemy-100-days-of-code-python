import tkinter as tk
import tkinter.messagebox as mb
import pwgen
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pw():
    generated_password = pwgen.password
    password_entry.insert(0, generated_password)
    # pyperclip project
    # to copy to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pw():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        mb.showerror(title="Error", message="You cannot leave empty inputs.")
        return

    is_ok = mb.askokcancel(
        title="hey", message=f"You entered:\n{website}\n{email}\n{password}\nIs it OK to save?")

    if is_ok:
        line = ','.join([website, email, password]) + '\n'

        with open('pw.txt', 'a', encoding='utf-8') as f:
            f.write(line)
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
window.config(padx=60, pady=60, bg='white')

# image
canvas = tk.Canvas(width=200, height=200, bg='white', highlightthickness=0)
p_image = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=p_image)
canvas.grid(row=0, column=1)

# website
website_label = tk.Label(text="Website")
website_label.grid(row=1, column=0, pady=10)

website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# email/username
email_label = tk.Label(text="Email/Username")
email_label.grid(row=2, column=0, pady=10)

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'email@email.com')

# password
password_label = tk.Label(text="Password")
password_label.grid(row=3, column=0, pady=10)

password_entry = tk.Entry(width=24)
password_entry.grid(row=3, column=1)

generate_button = tk.Button(text="Generate PW", command=generate_pw)
generate_button.grid(row=3, column=2)

# addbutton
add_button = tk.Button(text="Add password", width=35, command=save_pw)
add_button.grid(row=4, column=1, columnspan=2, pady=20)


window.mainloop()
