import tkinter
from tkinter import *
from tkinter import messagebox

if __name__ == "__main__":

    main_window = tkinter.Tk()
    main_window.title("Login")
    main_window.geometry("400x450")
    main_window.configure(bg = "royal blue")
    main_window.resizable(False, False)

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

    signup_button = tkinter.Button(main_window, text = "Sign Up", bg = "royal blue", font = ("Comic Sans MS", 12))
    signup_button.pack(side = RIGHT, anchor = S)

    main_window.mainloop()
