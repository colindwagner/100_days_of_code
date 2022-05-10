from tkinter import *

#import Tk class for a window
window = Tk()


#get the button to work
def button_clicked():
    miles = float(input.get())
    km = str(miles*1.609344)
    label_result.config(text=km)


window.title("mi to km calc")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#labels
label_miles = Label(text="Miles", font=('Arial', 12))
label_iseqto = Label(text="is equal to", font=('Arial', 12))
label_km = Label(text="Km", font=('Arial', 12))
label_result = Label(text="0", font=('Arial', 12))

#Create Button
button = Button(text="Calculate", command=button_clicked)

#Entry component
input = Entry(width=10)

#layouts
label_miles.grid(column=3,row=1)
label_iseqto.grid(column=1,row=2)
label_km.grid(column=4,row=2)
label_result.grid(column=2,row=2)
button.grid(column=1,row=3)
input.grid(column=1,row=1)



#keeps window on the screen
window.mainloop()