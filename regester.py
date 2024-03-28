import mysql.connector
from tkinter import messagebox,simpledialog
import tkinter as tk
from databes_creation import authenticate_user

# function to insert a new user into the database
def insert_user(first_name, last_name, email, password, username):
    # check if the user already exists in the database
    y = authenticate_user(first_name, last_name, email, password, username)
    if y==1:
        messagebox.showinfo("Success", "User added successfully!")
        reply = messagebox.askyesno("Log", "Do you want to log-in")
        if reply==True:
            root.destroy()
            import authentication_window
        else:
            return 0;
    elif y==0:
        messagebox.showerror("Error", "User already exists!")
    else:
        messagebox.showerror("Error-1054", "Try again later")


# function to handle form submission
def submit_form():
    user_check = []
    # get the form data
    first_name = entry_first_name.get().strip()
    last_name = entry_last_name.get().strip()
    email = entry_email.get().strip()
    password = entry_password.get()
    password_confirm = entry_password_confirm.get()
    username =entry_username.get().strip()
    terms_agreed = checkbutton_terms.get()

    # validate the form data
    if not first_name or not last_name or not email or not password or not password_confirm or not username:
        messagebox.showerror("Error", "All fields are required!")
    elif password != password_confirm:
        messagebox.showerror("Error", "Passwords do not match!")
    elif not terms_agreed:
        messagebox.showerror("Error", "Please agree to the terms and conditions.")
    else:

        root = tk.Tk()
        root.withdraw()

        # show a message box with an input dialog
        from email_verify import email_verification

        email_verification(email,user_check)
        print("#####")
        user_input = simpledialog.askstring("input the verification code sent to your email", "code: ")
        user_check.append(user_input)
        # print the user's input
        if user_check[0]==user_check[1]:
            messagebox.showinfo("seccess","you have registred into our application")
            # insert the user into the database
            insert_user(first_name, last_name, email, password, username)
        else:
            messagebox.showerror("Error","your code doesn't match with the message we sent you")

# create the main window
root = tk.Tk()
root.title("User Authentication Form")
root.geometry("400x500+350+100")




# create the form elements
label_first_name = tk.Label(root, text="First Name")
label_first_name.grid(row=0, column=0, padx=10, pady=10)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=10)

label_last_name = tk.Label(root, text="Last Name")
label_last_name.grid(row=1, column=0, padx=10, pady=10)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email")
label_email.grid(row=2, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password")
label_password.grid(row=3, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=3, column=1, padx=10, pady=10)

label_password_confirm = tk.Label(root, text="Confirm Password")
label_password_confirm.grid(row=4, column=0, padx=10, pady=10)
entry_password_confirm = tk.Entry(root, show="*")
entry_password_confirm.grid(row=4, column=1, padx=10, pady=10)
checkbutton_terms = tk.BooleanVar()

label_username = tk.Label(root, text="define a username")
label_username.grid(row=5, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=5, column=1, padx=10, pady=10)


checkbutton_terms = tk.BooleanVar()
checkbutton_terms.set(False)
checkbutton_terms_label = tk.Label(root, text="I agree to the terms and conditions:")
checkbutton_terms_label.grid(row=6, column=0, padx=10, pady=10)
checkbutton_terms_checkbox = tk.Checkbutton(root, variable=checkbutton_terms)
checkbutton_terms_checkbox.grid(row=6, column=1, padx=10, pady=10)

button_submit = tk.Button(root, text="Submit", command=submit_form, cursor="hand2")
button_submit.grid(row=7, column=1, padx=10, pady=10)

label_error = tk.Label(root, text="")
label_error.grid(row=8, column=1, padx=10, pady=10)

# start the main event loop
root.mainloop()