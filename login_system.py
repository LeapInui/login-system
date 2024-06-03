import tkinter
from tkinter import *
from tkinter import messagebox

def signup_window():

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

if __name__ == "__main__":

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
