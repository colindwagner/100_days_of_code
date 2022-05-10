import tkinter

#import Tk class for a window
window = tkinter.Tk()


#get the button to work
def button_clicked():
    my_label.config(text="Button got me clicked")
    print(input.get())


window.title("GUI program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#label
my_label = tkinter.Label(text="Label!", font=('Arial', 24, "bold"))
#place label
#my_label.pack()

#Create Button
button = tkinter.Button(text="Click Me", command=button_clicked)


#Entry component
input = tkinter.Entry(width=10)


#layouts
#pack, place, and grid
#my_label.place(x=150,y=0)

button.grid(column=1,row=6)
my_label.grid(column=0,row=1)

#keeps window on the screen
window.mainloop()