from tkinter import *

def miles_to_kilometeres():
    miles = float(miles_input.get())
    km = round(miles*1.6)
    kilometer_result.config(text = f"{km}")




window = Tk() 
window.title("MILES TO KM CONVERTER") 
window.config(padx=20,pady=20)

miles_input = Entry(width = 7) 
miles_input.grid(column = 1 , row = 0)

miles_label = Label(text = "Miles")
miles_label.grid(column = 2, row = 0)

is_equal_kabel = Label(text = "IS EQUALS TO")
is_equal_kabel.grid(column = 0, row =1 )

kilometer_result = Label(text = "0") 
kilometer_result.grid(column =1 , row = 1)

kilometer_label = Label(text = "KM")
kilometer_label.grid(column = 2, row = 1)


calculate_button = Button(text = "CALCULATE" , command = miles_to_kilometeres) 
calculate_button.grid(column = 1, row =2 )















window.mainloop()