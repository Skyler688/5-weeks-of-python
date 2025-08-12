# python3 week-3/tkinter-day-27/mile-to-kilometers/main.py

from tkinter import *

def calculate_km():
    try:
        mile = int(input.get())
        km = int(mile / 0.621371)
        label_km_val.config(text=km)
    except:
        # display error message to window
        warn = Label(text="ERROR INVALID INPUT", fg="red")
        warn.grid(row=3, column=1)
        
        window.after(2000, warn.destroy)   

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input = Entry()
input.config(width=10)
input.grid(row=0, column=1)

label_mile = Label(text="Miles")
label_mile.grid(row=0, column=2)

label_equal = Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_km_val = Label(text="0")
label_km_val.grid(row=1, column=1)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

calculate = Button(text="Calculate", command=calculate_km)
calculate.grid(row=2, column=1)


window.mainloop()



