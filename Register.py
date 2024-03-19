import tkinter as tk
import sqlite3
import db
def register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if password != confirm_password:
        status_label.config(text="Password does not match")
    else:
            conn = sqlite3.connect("user_database.db")
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()

            conn.close()

            status_label.config(text="Registered successfully")

            # Ẩn cửa sổ đăng ký sau khi đăng ký thành công
            register_window.destroy()
db.create_database()
# Tạo cửa sổ
register_window = tk.Tk()
register_window.geometry("600x400")
register_window.title("Register Form")

# Tạo các label và entry
username_label = tk.Label(register_window, text="Username:", font=("Helvetica", 17), fg="#333")
username_label.grid(row=0, column=0, padx=10, pady=5)

username_entry = tk.Entry(register_window, font=("Helvetica", 17), bd=2, relief=tk.FLAT)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(register_window, text="Password:", font=("Helvetica", 17), fg="#333")
password_label.grid(row=1, column=0, padx=10, pady=5)

password_entry = tk.Entry(register_window, font=("Helvetica", 17), show="*", bd=2, relief=tk.FLAT)
password_entry.grid(row=1, column=1, padx=10, pady=5)

confirm_password_label = tk.Label(register_window, text="Confirm Password:", font=("Helvetica", 17), fg="#333")
confirm_password_label.grid(row=2, column=0, padx=10, pady=5)

confirm_password_entry = tk.Entry(register_window, font=("Helvetica", 17), show="*", bd=2, relief=tk.FLAT)
confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

status_label = tk.Label(register_window, text="", fg="red")
status_label.grid(row=3, columnspan=2, padx=10, pady=5)

# Tạo nút đăng ký
register_button = tk.Button(register_window, text="Register", font=("Helvetica", 17), bg="#008CBA", fg="white", relief=tk.FLAT, command=register)
register_button.grid(row=4, columnspan=2, padx=10, pady=10)

register_window.mainloop()
