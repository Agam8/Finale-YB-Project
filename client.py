import tkinter as tk
import os
USER = ''
PASS = ''
LOGGED = False


class LoginScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.username_or_email = tk.StringVar()
        self.password = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Set window background color
        #self.master.configure(bg="#F9F9F9")


        # Create label and entry for username or email
        tk.Label(self, text="Username or Email:", font=("Arial", 14), bg="#F9F9F9").grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self.username_or_email, font=("Arial", 14)).grid(row=0, column=1, padx=10, pady=10)

        # Create label and entry for password
        tk.Label(self, text="Password:", font=("Arial", 14), bg="#F9F9F9").grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self.password, show="*", font=("Arial", 14)).grid(row=1, column=1, padx=10, pady=10)

        # Create login button
        login_button = tk.Button(self, text="Login", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.login)
        login_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        login_button.config(width=10, height=1)

        # Add logo image
        logo_image = tk.PhotoImage(file=f"{os.path.abspath(os.getcwd())}/login/agamusic-logo.png")
        logo_label = tk.Label(self, image=logo_image, bg="#F9F9F9")
        logo_label.image = logo_image
        logo_label.grid(row=0, column=2, rowspan=3, padx=20, pady=100)

        # Pack the frame
        self.pack()

    def validate_credentials(self,username,password):
        print(f'recv {username}, {password}')
        # Check that username is not empty
        if not username:
            return False, "Username cannot be empty"
        # Check that password is at least 8 characters long
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"

        # Check that password contains at least one uppercase letter, one lowercase letter, and one number
        has_uppercase = False
        has_lowercase = False
        has_number = False
        for c in password:
            if c.isupper():
                has_uppercase = True
            elif c.islower():
                has_lowercase = True
            elif c.isnumeric():
                has_number = True

        if not (has_uppercase and has_lowercase and has_number):
            return False, "Password must contain at least one uppercase letter, one lowercase letter, and one number"

        # If all checks pass, return True and an empty string for the error message
        return True, ""

    def login(self):
        global LOGGED
        # Get the username or email and password values and perform login logic here
        username_or_email = self.username_or_email.get()
        password = self.password.get()
        valid, error = self.validate_credentials(username_or_email, password)

        if valid:
            print(f"Logging in with username or email {username_or_email} and password {password}")
            error_label = tk.Label(self, text="LOGGING IN", font=("Arial", 14))
            error_label.grid(row=3, column=0, padx=10, pady=10, rowspan=3, columnspan=3)
            LOGGED = True
            self.after(2000, lambda: New_Window())

        else:
            """error_label = tk.Label(self, text=error, font=("Arial", 14))
            error_label.grid(row=3, column=0, padx=10, pady=10, rowspan=3, columnspan=3)
            # Add the following line to remove the error message after 2 seconds
            self.after(2000, lambda: error_label.destroy())"""
            tk.messagebox.showerror()

    def clear_frame(self):
        for widgets in self.winfo_children():
            widgets.destroy()

    def set_user(self, username_or_email):
        self.username_or_email.set(username_or_email)

    def get_user(self):
        return self.username_or_email.get()

    def set_password(self, password):
        self.password.set(password)

    def get_password(self):
        return self.password.get()

class MainScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.username_or_email = tk.StringVar()
        self.password = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):


def main():
    root = tk.Tk()
    root.geometry("1500x700")
    login_screen = LoginScreen(root)
    login_screen.set_user("enter you username or email")
    login_screen.set_password("enter your password")

    root.mainloop()
    
    user = login_screen.get_user()
    password = login_screen.get_password()


if __name__ == "__main__":
    main()
