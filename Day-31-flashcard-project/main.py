import tkinter as tk
import csv
import random

BACKGROUND_COLOR = "#B1DDC6"
font1 = ('Ariel', 40, 'italic')
font2 = ('Ariel', 60, 'bold')

word_list = []
ok_words = []
new_word = {'French': 'french', 'English': 'english'}
timer = None

# read csv file without pandas


def read_csv_file():
    global word_list
    # create list of dictionaries
    # [
    #     {
    #         'French': 'frenchword',
    #         'English': 'englishword'
    #     }
    # ]

    try:
        f = open('data/words_to_learn.csv', encoding='utf-8')

    except FileNotFoundError:
        f = open('data/french_words.csv', encoding='utf-8')

    finally:
        reader = csv.reader(f)
        for row in reader:
            if not row[0] == 'French':
                new_dict = {
                    'English': row[1],
                    'French': row[0]
                }

                word_list.append(new_dict)

        f.close()


def create_new_flashcard():
    # get new word
    global new_word
    global word_list
    global timer

    window.after_cancel(timer)
    random_index = random.randint(0, len(word_list)-1)
    new_word.update(
        {'English': word_list[random_index]['English'], 'French': word_list[random_index]['French']})
    # update UI
    # card_front
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=new_word['French'], fill='black')
    timer = window.after(3000, flip)


def flip():
    # card back
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(card_word, text=new_word['English'], fill="white")


def save_list():
    global word_list

    with open('data/words_to_learn.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['French', 'English'])
        for word in word_list:
            writer.writerow([word['French'], word['English']])


def wrong():
    create_new_flashcard()


def right():
    global new_word
    global word_list
    # remove word
    word_list.remove(new_word)
    save_list()
    create_new_flashcard()


read_csv_file()
# -------------------------------UI------------------------------
window = tk.Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")

# canvas
canvas = tk.Canvas(width=800, height=526,
                   highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text='French', font=font1)
card_word = canvas.create_text(400, 263, text=new_word['French'], font=font2)
timer = window.after(3000, flip)
create_new_flashcard()

# buttons
x_image = tk.PhotoImage(file="images/wrong.png")
button_x = tk.Button(image=x_image, highlightthickness=0,
                     border=0, command=wrong)
button_x.grid(row=1, column=0)

y_image = tk.PhotoImage(file="images/right.png")
button_y = tk.Button(image=y_image, highlightthickness=0,
                     border=0, command=right)
button_y.grid(row=1, column=1)

window.mainloop()
