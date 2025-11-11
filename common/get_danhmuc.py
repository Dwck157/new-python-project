from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_to_mysql


def get_all_danhmuc():
    """
    Lấy toàn bộ danh sách danh mục trong bảng 'danhmuc'
    Trả về list các tuple (id, ten, mota)
    """
    connection = connect_to_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối CSDL.")
        return []

    try:
        cursor = connection.cursor()
        sql = "SELECT id, ten_danhmuc, mo_ta FROM danhmuc"
        cursor.execute(sql)
        result = cursor.fetchall()

        if len(result) == 0:
            print("⚠️ Chưa có danh mục nào trong CSDL.")
        else:
            print("📋 Danh sách danh mục:")
            for row in result:
                print(f"- ID: {row[0]}, Tên: {row[1]}, Mô tả: {row[2]}")
        return result

    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối MySQL.")
