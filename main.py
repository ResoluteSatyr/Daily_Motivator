import datetime as dt
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
color_list = ["red", "pink", "purple", "orange", "black"]
# It gives the current time and date
now = dt.datetime.now()
day = now.weekday()
quotes_list = []
NEW_DAY = ""
Q = ""


def current_day():
    global NEW_DAY
    if day == 0:
        NEW_DAY = "Monday"
    elif day == 1:
        NEW_DAY = "Tuesday"
    elif day == 2:
        NEW_DAY = "Wednesday"
    elif day == 3:
        NEW_DAY = "Thursday"
    elif day == 4:
        NEW_DAY = "Friday"
    elif day == 5:
        NEW_DAY = "Saturday"
    elif day == 6:
        NEW_DAY = "Sunday"
    return NEW_DAY


current_day()
# print(new_day)
with open("quotes.txt", "r") as quotes:
    daily_quotes = quotes.readlines()
    for quote in daily_quotes:
        quotes_list.append(quote)


def get_quote():
    global Q
    Q = random.choice(quotes_list)
    canvas.itemconfig(display_quote, text=Q)
    return Q


# ______________________________________________ UI SETUP _____________________________________________________#
offset = (100, 100)
window = Tk()
window.title("Daily Motivator")
window.config(pady=20, background="lightblue")
canvas = Canvas(width=1000, height=300, background="light yellow", highlightthickness=0)
canvas.create_text(500, 50, text=NEW_DAY, font=("Ariel", 40, "bold"), fill=random.choice(color_list), width=950)
display_quote = canvas.create_text(500, 150, text=Q, font=("Ariel", 10, "bold"), fill="green")
canvas.grid(column=0, row=0)


"""Buttons"""
next_quote = Button(text="Next Quote", command=get_quote, fg="red")
next_quote.config(background="lightblue")
next_quote.grid(column=0, row=3,)

get_quote()
window.mainloop()
