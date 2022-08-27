from tkinter import *
from tkinter import messagebox
window = Tk()

def calculate():
    
    subject = (subject_entry.get()).upper()
    conducted = float(conducted_entry.get())
    attended = float(attended_entry.get())
    if attended<=conducted:
        h=0
        while (attended+h)/(conducted+h) <= 0.75:
            if (attended+h)/(conducted+h) >= 0.75:
                d=(h)
                messagebox.showinfo(title="MARGIN", message=f"For {subject} you require  {d} hours.")
                
                break
            else:
                h+=1
    
        h=0
        while (attended+h)/(conducted+h) >= 0.75:
            if (attended)/(conducted+h) <=0.75:
                c= (h-1)
                messagebox.showinfo(title="MARGIN", message=f"For {subject} you have margin of {c} hour.")
                
                break
            else:
                h+=1
                
    else:
        messagebox.showinfo(title="Wrong", message= "Attended cannot be more than conducted")
    
    

   
window.title("Attendance Margin")
window.config(padx=50, pady=50)

subject_label = Label(text = "Subject:")
subject_label.grid(row=1, column=0)
conducted_label = Label(text="Hours Conducted:")
conducted_label.grid(row=2, column=0)
attended_label = Label(text="Hours Attended:")
attended_label.grid(row=3, column=0)


subject_entry = Entry(width=30)
subject_entry.grid(row=1, column=1)
subject_entry.focus()

conducted_entry = Entry(width=30)
conducted_entry.grid(row=2, column=1)

attended_entry = Entry(width=30)
attended_entry.grid(row=3, column=1)

calculate_button = Button(text="calculate", width=36, command=calculate)
calculate_button.grid(row=4, column=1, columnspan=2)

window.mainloop()