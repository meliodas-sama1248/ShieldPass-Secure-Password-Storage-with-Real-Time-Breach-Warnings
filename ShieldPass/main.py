import tkinter as tk
from tkinter import messagebox
from db_manager import setup_database, save_password, get_password
from encryption import encrypt_password, decrypt_password
from breach_checker import check_password_breach
from logger import log_event

# Initialize database
setup_database()

def save_action():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Breach check
    if check_password_breach(password):
        log_event("BREACH_ALERT", f"Password for {website} was found in a data breach!")
        messagebox.showwarning("Breach Alert", "⚠️ This password has been breached! Use a different one.")
        return

    encrypted_password = encrypt_password(password)

    # Try saving the password
    success = save_password(website, username, encrypted_password)
    if not success:
        log_event("DUPLICATE_SAVE", f"Tried saving duplicate entry for {website} - {username}")
        messagebox.showwarning("Duplicate Entry", "⚠️ A password for this website already exists!")
        return

    log_event("PASSWORD_SAVED", f"Saved password for {website} - {username}")
    messagebox.showinfo("Success", "✅ Password saved successfully!")

def retrieve_action():
    website = website_entry.get()
    result = get_password(website)

    if result:
        username, encrypted_password = result
        password = decrypt_password(encrypted_password)
        log_event("PASSWORD_RETRIEVED", f"Retrieved password for {website} - {username}")
        messagebox.showinfo("Password Found", f"Username: {username}\nPassword: {password}")
    else:
        log_event("PASSWORD_NOT_FOUND", f"Tried retrieving password for {website}, but it was not found.")
        messagebox.showwarning("Not Found", "No password found for this website.")

# GUI Window
root = tk.Tk()
root.title("Secure Password Manager")

tk.Label(root, text="Website:").grid(row=0, column=0)
tk.Label(root, text="Username:").grid(row=1, column=0)
tk.Label(root, text="Password:").grid(row=2, column=0)

website_entry = tk.Entry(root)
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

website_entry.grid(row=0, column=1)
username_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)

tk.Button(root, text="Save Password", command=save_action).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Retrieve Password", command=retrieve_action).grid(row=4, column=0, columnspan=2)

root.mainloop()
