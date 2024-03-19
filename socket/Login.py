import tkinter as tk
import sqlite3
import importlib
from tkinter import messagebox

def authenticate(username, password):
    try:
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()

        # Thực hiện truy vấn SQL để kiểm tra thông tin đăng nhập
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            return True  # Đăng nhập thành công
        else:
            return False  # Đăng nhập thất bại
    except sqlite3.Error as e:
        messagebox.showerror("Error:", e)
        return False  # Đăng nhập thất bại


# Tạo cửa sổ
root = tk.Tk()
root.geometry("600x600")
root.title("Đăng nhập")

# Tạo các widget
username_label = tk.Label(text="Username:", font=("Helvetica", 17), fg="#333")
username_entry = tk.Entry(font=("Helvetica", 17), bd=2, relief=tk.FLAT)

password_label = tk.Label(text="Password:", font=("Helvetica", 17), fg="#333")
password_entry = tk.Entry(font=("Helvetica", 17), show="*", bd=2, relief=tk.FLAT)

login_button = tk.Button(text="Login", font=("Helvetica", 17), bg="#4CAF50", fg="white", relief=tk.FLAT)
register_button = tk.Button(text="Register", font=("Helvetica", 17), bg="#008CBA", fg="white", relief=tk.FLAT)

# Xử lý sự kiện
def login_handler():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        if authenticate(username, password):
            chat_module = importlib.import_module("client")
            root.destroy()  # Đóng cửa sổ đăng nhập
            chat_module.start()  # Gọi hàm từ client.py
        else:
            # Thông báo đăng nhập không thành công
            tk.messagebox.showerror("Error", "Invalid username or password")

def register_handler():
    # Chuyển hướng đến trang đăng ký
    if __name__ == "__main__":
        register_module = importlib.import_module("Register")
        register_module.create_register_window()  # Assuming create_register_window in Register.py

def navigate_to_home():
    # Chuyển hướng đến trang chủ
    pass

# Đặt vị trí widget
username_label.place(x=150, y=200)
username_entry.place(x=300, y=200)

password_label.place(x=150, y=250)
password_entry.place(x=300, y=250)

login_button.place(x=250, y=300)
register_button.place(x=250, y=350)

# Bắt đầu vòng lặp chương trình
def main():
    login_button.config(command=login_handler)
    register_button.config(command=register_handler)
    root.mainloop()

if __name__ == "__main__":
    main()
