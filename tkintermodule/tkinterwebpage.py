from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import random
tk=Tk()
tk.geometry("400x400")
style=ttk.Style(tk)
style.theme_use('clam')
tk.title('first web page')
cal=Calendar(tk,selectmode='day',year=2022,month=1,day=11)
cal.pack(pady=10,fill='both',expand=True)

def datePicker():
    date.config(text="selected date is : "+cal.get_date())



tk.mainloop()

