from tkinter import *
from verification import verify
from PIL import ImageTk, Image

# Function to regestrate

def resizer(e):
    global bg1, resized_bg, new_bg
    bg1 = Image.open("dancing.jpg")

    #RESIZE THE IMAGE
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)

    #REDEFINE THE IMAGE
    new_bg = ImageTk.PhotoImage(resized_bg)


    #ADD BACK TO LABEL
    canvas.create_image(0, 0, image=new_bg, anchor='nw')

def regester_bt():
    root.destroy()
    import regester
    print("switch")

# Function to authenticate user
def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are correct
    x = verify(username, password)
    if x ==1 :
        result_label.config(text="Authentication successful", fg="green")
    else:
        result_label.config(text="Authentication failed", fg="red")

# Create main window
root = Tk()

root.title("Authentication")
root.geometry("800x500+200+75")
root.config(bg="black")
#root.resizable(0, 0)
# Load background image
bg_image = Image.open("2.jpg")
bg_image = bg_image.resize((800, 500))
bg_image = ImageTk.PhotoImage(bg_image)

#@@@@
# Create background label
canvas = Canvas(root,width=800, height=500)
canvas.pack(fill= "both",expand=True)
canvas.create_image(0,0,image=bg_image,anchor='nw')

#@@@@frame

registerFrame = Frame(root, width=240, height=300, bg='#0B193C', highlightbackground='#0B1975', highlightthickness=1)
registerFrame.place(x=300, y=170)

#title
username_label = Label(registerFrame, text="Registration Form", font=('arial',15,'bold'),fg="#9C9291", bg='#0B193C')
username_label.place(x=120, y=20, anchor=CENTER)

# Create username label and entry
username_label = Label(registerFrame, text="Username", fg="#cececd",bg='#0B193C', font=("Montserrat", 9), borderwidth=0)
username_label.place(relx=0.15, rely=0.41, anchor=CENTER)

username_entry = Entry(registerFrame, bg="#8B0000", fg="white")
username_entry.place(relx=0.58, rely=0.41, anchor=CENTER)

# Create password label and entry
password_label = Label(registerFrame, text="Password", bg='#0B193C', fg="#cececd", font=("Montserrat", 9))
password_label.place(relx=0.15, rely=0.52, anchor=CENTER)

password_entry = Entry(registerFrame, show="*", bg="#8B0000", fg="white")
password_entry.place(relx=0.58, rely=0.52, anchor=CENTER)

# Create login button
login_button = Button(registerFrame, text="Login", command=authenticate, bg="#8B0000", fg="white", width=30, cursor="hand2")
login_button.place(relx=0.52, rely=0.75, anchor=CENTER)

# Creat regestration buton
regester_button = Button(registerFrame, text="I Don't Have An Account", border=0, command=regester_bt,bg='#0B193C', cursor="hand2",fg="#cececd", font=("Montserrat", 7, "bold"))
regester_button.place(relx=0.73, rely=0.85, anchor=CENTER)

# Create label for displaying authentication result
result_label = Label(registerFrame, fg="white", bg='#0B193C')
result_label.place(relx=0.52, rely=0.65, anchor=CENTER)

# Set window size and run main loop

root.geometry("800x500")
root.bind('<Configure>', resizer)

root.mainloop()

