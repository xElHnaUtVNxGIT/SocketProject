import sqlite3

def create_database():
    # Tạo kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('user_database.db')

    # Tạo con trỏ để thực hiện các truy vấn SQL
    cursor = conn.cursor()
    sqlTable="""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )"""
    sqlSelect = "SELECT * FROM users"
    
    # Tạo bảng trong cơ sở dữ liệu để lưu trữ thông tin đăng ký
    cursor.execute(sqlTable)
    
    
    # Thực hiện truy vấn SELECT để lấy dữ liệu từ bảng users
    #cursor.execute(sqlSelect)
    #print(cursor.fetchall())

    # Lưu thay đổi
    conn.commit()

    # Đóng kết nối khi đã hoàn thành
    conn.close()

create_database()
