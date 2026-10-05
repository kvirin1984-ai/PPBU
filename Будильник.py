from tkinter import *
from tkinter import messagebox as mb
import time

import pygame
import pygame as pg

pg.mixer.init()
pg.mixer.music.load('music.mp3')



def tick():
    global time_alarm
    current_time = time.strftime("%H:%M:%S")
    if (time_alarm == current_time or
            time_alarm == time.strftime("%H:%M") or
            time_alarm == time.strftime("%H")):
        time_alarm = ''
        pg.mixer.music.play()
    screen_time.after(1000, tick)
    screen_time.config(text=current_time)


def on_click():
    global time_alarm
    time_alarm = entry_time.get().strip()

    mb.showinfo('Включение будильника', f'Будильник включен на {time_alarm}')


def off_click():
    global time_alarm
    time_alarm = ''
    entry_time.delete(0, 'end')
    pg.mixer.music.stop()
    mb.showwarning('Выключение будильника', f'Будильник выключен')


time_alarm = ''

root = Tk()

# f1 = Frame(root)
# f1.pack(side=TOP)

root.title('Будильник')
root.config(background='black')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 500
Y = 300
root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT // 2 - Y // 2 - 25}")

screen_time = Label(text='00:00:00', font='Arial 50')

screen_time.config(bg='black', fg='lime')
screen_time.pack()

entry_time = Entry(root, width=15, font='Arial 20', justify='center')
entry_time.pack()

on = Button(root, text='Включить', font=('Arial', 15), command=on_click)
on.pack(pady=10)

off = Button(root, text='Выключить', font=('Arial', 15), command=off_click)
off.pack()

tick()

root.mainloop()
