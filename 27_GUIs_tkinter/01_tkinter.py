import tkinter

#import Tk class for a window
window = tkinter.Tk()



window.title("GUI program")
window.minsize(width=500, height=300)

#label
my_label = tkinter.Label(text="Label!", font=('Arial', 24, "bold"))
#place label
my_label.pack()


#get the button to work
def button_clicked():
    my_label.config(text="Button got me clicked")
    print(input.get())

#Create Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


#Entry component
input = tkinter.Entry(width=10)
input.pack()



#keeps window on the screen
window.mainloop()