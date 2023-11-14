from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("960x650")
window.configure(bg = "#404040")
canvas = Canvas(
    window,
    bg = "#404040",
    height = 650,
    width = 960,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    480.0, 57.5,
    text = "LinkedIn Scrapper Prototype",
    fill = "#ffffff",
    font = ("RobotoRoman-Regular", int(40.0)))

canvas.create_text(
    480.0, 162.0,
    text = "Please login to your LinkedIn Account first",
    fill = "#ffffff",
    font = ("RobotoRoman-Regular", int(32.0)))

canvas.create_text(
    244.0, 239.0,
    text = "Email",
    fill = "#ffffff",
    font = ("RobotoRoman-Regular", int(32.0)))

entry0_img = PhotoImage(file = f"GUI/img_textBoxEntry.png")
entry0_bg = canvas.create_image(
    480.5, 239.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f1f3ff",
    highlightthickness = 0)

entry0.place(
    x = 320.0, y = 209,
    width = 321.0,
    height = 59)

canvas.create_text(
    213.0, 334.0,
    text = "Password",
    fill = "#ffffff",
    font = ("RobotoRoman-Regular", int(32.0)))

entry1_img = PhotoImage(file = f"GUI/img_textBoxEntry.png")
entry1_bg = canvas.create_image(
    480.5, 334.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

entry1.place(
    x = 320.0, y = 304,
    width = 321.0,
    height = 59)

canvas.create_text(
    223.0, 430.0,
    text = "File path",
    fill = "#ffffff",
    font = ("RobotoRoman-Regular", int(32.0)))

entry2_img = PhotoImage(file = f"GUI/img_textBoxEntry.png")
entry2_bg = canvas.create_image(
    480.5, 429.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

entry2.place(
    x = 320.0, y = 399,
    width = 321.0,
    height = 59)

entry3_img = PhotoImage(file = f"GUI/img_textBoxLong.png")
entry3_bg = canvas.create_image(
    480.0, 514.0,
    image = entry3_img)

entry3 = Text(
    bd = 0,
    bg = "#f1f3ff",
    highlightthickness = 0)

entry3.place(
    x = 142.0, y = 479,
    width = 676.0,
    height = 68)

img0 = PhotoImage(file = f"GUI/img_login.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 291, y = 568,
    width = 180,
    height = 55)

img1 = PhotoImage(file = f"GUI/img_scrape.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 489, y = 568,
    width = 180,
    height = 55)

window.resizable(False, False)
window.mainloop()
