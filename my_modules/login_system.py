# Create a Login System.

# Import tkinter and messagebox (which allows the creation of a GUI).
import tkinter as tk
from tkinter import messagebox

# Start of program.

# Create a class called LoginSystem.
class LoginSystem:

    # Create a def __init__ function that takes in self and master.
    def __init__(self, master):
        self.master = master
        self.master.title("Login System")
        self.master.geometry("300x150")

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

        self.attempts = 0
        self.max_attempts = 3

    # Create a def login function that takes in self.
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.check_login(username, password):
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.master.destroy()
        else:
            self.attempts += 1
            if self.attempts >= self.max_attempts:
                self.lock_user_out()
            else:
                messagebox.showwarning("Login Failed", "Incorrect login. Please try again.")

    # Create a def check_login function that takes in self, username, and password.
    def check_login(self, username, password):
       
        valid_username = "Slycommie80"
        valid_password = "MarxistLeninist"

        return username == valid_username and password == valid_password

    # Create a def lock_user_out function that takes in self.
    def lock_user_out(self):
        messagebox.showerror("Login Failed", "You have reached the maximum number of login attempts.")
        self.master.destroy()

# Create an if __name__ == "__main__" statement that calls the LoginSystem class.
if __name__ == "__main__":
    root = tk.Tk()
    login_system = LoginSystem(root) # Object of LoginSystem class.
    root.mainloop()

# End of program.