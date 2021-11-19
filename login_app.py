#!/usr/bin/env python3
# Justin Clark
# 2021/11/19

# login_app.py

import tkinter as tk
import time

class LoginApp:
    ''' GUI Program that takes user input and stores it as a dictionary '''

    def login(self):
        ''' Check that username and password are both in the credentials dictionary '''
        if self.username not in self.valid_credentials.keys():
            print("You're not on the list you numpty")
            return

        print("Look who's here! Bozo the clown -_-")
        print("Prepare for liftoff in...")

        for i in range(5, 0, -1): # count down from 5 to 0
            print(str(i) + "...")
            time.sleep(.5)
        
        print("You all crashed and died. The end.")

        return # loop back to login

    def create_account(self):
        ''' adds the username and password variables to the dictionary '''
        
        self.username = self.username.lower() # pylance predicts an error, but it's wrong.. ([1] See bottom of script)

        if self.username not in self.valid_credentials.keys():
            self.valid_credentials[self.username] = self.password # same error as [1]

            if self.DEBUG:
                print("Credentials: ")
                print(self.valid_credentials)
        else:
            print("Account already exists")

    def on_key_press(self, action):
        self.username = self.stringvar_1.get().strip()
        self.username = self.username.lower()

        self.password = self.stringvar_2.get().strip()

        if action == "create":
            self.create_account()
        else:
            self.login()

    def exit(self):
        ''' destory the instance of the window '''
        self.master.destroy()

    def debug(self):
        self.DEBUG = not self.DEBUG
        self.stringvar_3.set(f" debug mode {self.DEBUG}")

    def __init__(self, master):
        ''' Init Function '''
        self.DEBUG = False

        if self.DEBUG:
            print("tkinter_base Initialized")

        self.master = master

        # allowed credentials
        self.valid_credentials = {
            "justin" : "clark",
            "elon" : "musk",
            "alec" : "baldwin"
        }

        # Pre-Widget Window Modificatins
        master.title("Rocket Ship Registration")
        master.geometry("600x500")

        # Temp Preliminary Variables
        self.username = None
        self.password = None

        # Frame that houses widgets
        self.mainframe = tk.Frame(master)

        # Username and Password label widgets inside the frame
        self.label_01 = tk.Label(self.mainframe,
            text="Username"
        )

        self.label_02 = tk.Label(self.mainframe,
            text="Password"
        )

        self.stringvar_3 = tk.StringVar()

        self.label = tk.Label(self.mainframe,
            textvariable=self.stringvar_3
        )

        # Bottom buttons
        self.button_submit = tk.Button(self.mainframe, text="Submit", bg="#49ba3a")
        self.button_create = tk.Button(self.mainframe, text="Create Account")
        self.button_exit = tk.Button(
            self.mainframe,
            text="Exit",
            command= self.exit
        )
        self.button_debug = tk.Button(self.mainframe, text="Debug")

        # StringVar types for Entries
        self.stringvar_1 = tk.StringVar()
        self.stringvar_2 = tk.StringVar()

        self.text_01 = tk.Entry(self.mainframe,
            textvariable=self.stringvar_1
        )

        self.text_02 = tk.Entry(self.mainframe,
            textvariable=self.stringvar_2
        )

        # Set StringVar placeholder values for Entries
        self.stringvar_1.set("Username")
        self.stringvar_2.set("Password")

        self.stringvar_3.set("")

        # ==== Packing to fit the display ====

        self.label.pack(expand=True)

        # Username Widgets
        self.label_01.pack(expand=True)
        self.text_01.pack(expand=True)

        # Password Widgets
        self.label_02.pack(expand=True)
        self.text_02.pack(expand=True)

        # Submit + Create buttons
        self.button_submit.pack(expand=True)
        self.button_create.pack(expand=True)
        self.button_exit.pack(expand=True)

        # Debug button
        self.button_debug.pack(expand=True)

        # Tk Frame
        self.mainframe.pack(padx=200, pady=100)

        self.master.bind(
            '<Return>', lambda event: self.on_key_press("login")
        )

        self.button_submit.bind(
            '<Button>', lambda event: self.on_key_press("login")
        )

        self.button_create.bind(
            '<Button>', lambda event: self.on_key_press("create")
        )

root = tk.Tk()
LoginApp(root)
root.mainloop()

# [1] value is empty at the time of the command being run but it gets turned into a string with the tkinter string var