import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
import bcrypt

def signup_window():

    # Register function
    def register():

        # Validation
        if regname_entry.get() == "" or regpass_entry.get() == "":
            messagebox.showerror("Error", "All fields are required")

        elif regpass_entry.get() != confirmregpass_entry.get():
            messagebox.showerror("Error", "Passwords do not match")

        else:
            cursor.execute("SELECT username FROM users WHERE username = ?", [regname_entry.get()])
            if cursor.fetchone() is not None:
                messagebox.showerror("Error", "Username already exists")
            else:
                encoded_pass = regpass_entry.get().encode("UTF-8")
                hashed_pass = bcrypt.hashpw(encoded_pass, bcrypt.gensalt()) # Hash password

                cursor.execute("INSERT INTO users VALUES (?, ?)", [regname_entry.get(), hashed_pass])
                conn.commit()
                messagebox.showinfo("Success", "Account registration is successful")
                regname_entry.delete(0, END)
                regpass_entry.delete(0, END)
                confirmregpass_entry.delete(0, END)
                back()

    # Functionality for back button
    def back():
        signup_window.destroy()
        main_window.deiconify()

    main_window.iconify()

    # Sign up window to register
    signup_window = tkinter.Tk()
    signup_window.title("Sign Up")
    signup_window.geometry("400x400")
    signup_window.configure(bg = "royal blue")
    signup_window.resizable(False, False)

    regname_label = tkinter.Label(signup_window, text = "Enter username", font = ("Comic Sans MS", 15))
    regname_label.configure(bg = "royal blue")
    regname_label.pack()
    regname_entry = tkinter.Entry(signup_window)
    regname_entry.pack()

    regpass_label = tkinter.Label(signup_window, text = "Enter password", font = ("Comic Sans MS", 15))
    regpass_label.configure(bg = "royal blue")
    regpass_label.pack()
    regpass_entry = tkinter.Entry(signup_window, show = "*")
    regpass_entry.pack()

    confirmregpass_label = tkinter.Label(signup_window, text = "Confirm password", font = ("Comic Sans MS", 15))
    confirmregpass_label.configure(bg = "royal blue")
    confirmregpass_label.pack()
    confirmregpass_entry = tkinter.Entry(signup_window, show = "*")
    confirmregpass_entry.pack()

    registerButton = tkinter.Button(signup_window, text = "Register", font = ("Comic Sans MS", 12))
    registerButton.configure(bg = "royal blue")
    registerButton.pack()

    backButton = tkinter.Button(signup_window, text = "Back", font = ("Comic Sans MS", 12), command = back)
    backButton.configure(bg = "royal blue")
    backButton.pack(side = LEFT, anchor = S)

if __name__ == "__main__":

    # Login function
    def login():
        if username_entry.get() == "" or password_entry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            cursor.execute("SELECT password FROM users WHERE username = ?", [username_entry.get()])
            result_password = cursor.fetchone()
            if result_password:
                if bcrypt.checkpw(password_entry.get().encode("UTF-8"), result_password[0]):
                    messagebox.showinfo("Success", "Login successful")
                    main_window.destroy()
                else:
                    messagebox.showerror("Error", "Invalid password")
            else:
                messagebox.showerror("Error", "Invalid username")

    # Create database
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL, password TEXT NOT NULL)")

    # Main log in window
    main_window = tkinter.Tk()
    main_window.title("Login")
    main_window.geometry("400x450")
    main_window.configure(bg = "royal blue")
    main_window.resizable(False, False)

    banner = tkinter.PhotoImage(file = "resources/banner.png")
    banner_image = tkinter.Label(main_window, image = banner, bg = "royal blue")
    banner_image.pack()

    username_label = tkinter.Label(main_window, text = "Username", bg = "royal blue", font = ("Comic Sans MS", 20))
    username_label.pack()
    username_entry = tkinter.Entry(main_window)
    username_entry.pack()

    password_label = tkinter.Label(main_window, text = "Password", bg = "royal blue", font = ("Comic Sans MS", 20))
    password_label.pack()
    password_entry = tkinter.Entry(main_window, show = "*")
    password_entry.pack()

    login_button = tkinter.Button(main_window, text = "Login", bg = "royal blue", font = ("Comic Sans MS", 12))
    login_button.pack()

    signup_button = tkinter.Button(main_window, text = "Sign Up", bg = "royal blue", font = ("Comic Sans MS", 12), command = signup_window)
    signup_button.pack(side = RIGHT, anchor = S)

    main_window.mainloop()
