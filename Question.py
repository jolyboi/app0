from tkinter import * 
import random 

root = Tk()

root.title("Question")
root.geometry("800x600")
root.config(bg="lightblue")

# Functions 
def my_click():
    clicked_label = Label(button_frame, text='Well, if you say so.', bg='lightblue', font=('Helvetica', 60), fg='red')
    clicked_label.pack() 
    yes_button.config(state=DISABLED)


def move_button(event):
    new_x = random.randint(0, button_frame.winfo_width() - no_button.winfo_width())
    new_y = random.randint(0, button_frame.winfo_height() - no_button.winfo_width())
       
    no_button.place(x=new_x, y=new_y)

        
# The constituents 

my_label = Label(root, text="What is 2x2?", bg="lightblue", font=("Helvetica", 40), fg='black')


button_frame = Frame(root, bg='lightblue')
button_frame.config(width=800, height=800)


yes_button = Button(button_frame, bg='green', text="Five", padx=20, pady=3, font=("Arial", 20), command=my_click, fg='red')
no_button = Button(button_frame, text='Four', padx=23, pady=3, font=("Arial", 20), fg='green')

# placing buttons in the frame 

yes_button.place(x=230, y=80)  
no_button.place(x=430, y=80)


# shove everything onto the screen 
my_label.pack(pady=10) 
button_frame.pack(pady=100)


no_button.bind("<Enter>", move_button)
root.mainloop()
