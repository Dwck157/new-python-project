import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    """
    Hàm kết nối đến MySQL.
    Trả về đối tượng kết nối nếu thành công, ngược lại trả về None.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,  # cổng mặc định của MySQL
            user='root',
            passwd='',
            database='qlthuocankhang'
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
    except Error as e:
        print(f"❌ Lỗi khi kết nối MySQL: {e}")
    return connection


# --- Ví dụ sử dụng ---
# if __name__ == "__main__":
#     conn = connect_to_mysql("localhost", "root", "", "ten_database_cua_ban")
#
#     if conn:
#         # Thực thi thử 1 truy vấn
#         cursor = conn.cursor()
#         cursor.execute("SHOW TABLES;")
#         for tb in cursor:
#             print(tb)
#         cursor.close()
#         conn.close()
