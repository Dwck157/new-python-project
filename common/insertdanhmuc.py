
from ketnoidb.ketnoi_mysql import connect_to_mysql
from mysql.connector import Error

def insert_danhmuc(tendanhmuc, mota=None):
    """
    Thêm mới 1 danh mục vào bảng 'danhmuc'
    :param tendanhmuc: Tên danh mục
    :param mota: Mô tả (tùy chọn)
    """
    connection = connect_to_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối CSDL.")
        return

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)"
        data = (tendanhmuc, mota)
        cursor.execute(sql, data)
        connection.commit()
        print("✅ Thêm danh mục thành công!")
    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối MySQL.")