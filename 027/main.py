from tkinter import *

window = Tk()
window.title("This is the new window")
window.minsize(width=500, height=300)



# Label
my_label = Label(text="What is the label here?", font=("Arial", 15))
my_label.grid(column=1, row=0)

# Entries
entry = Entry(width=14)
#Add some text to begin with
entry.insert(END, string="First name")
#Gets text in entry
print(entry.get())
entry.grid(column=2, row=1)

input = Entry(width=14)
input.insert(END, string="Last name")
input.grid(column=2, row=2)


#Buttons
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    #my_label.config(text=new_text)

button = Button(text="Press here", command=button_clicked)
button.grid(column=3,row=3)

window.mainloop()
