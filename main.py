import random
import string
import tkinter as tk

root = tk.Tk()
root.title('Password Generator')
root.mainloop()


def generate_password(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


password_length = int(input("Enter the length of the password: "))

password = generate_password(password_length)
print(f"Generated Password: {password}")