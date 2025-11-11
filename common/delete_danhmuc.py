from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_to_mysql


def delete_danhmuc(id_danhmuc):
    """
    Xóa danh mục theo ID
    :param id_danhmuc: ID của danh mục cần xóa
    """
    connection = connect_to_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối CSDL.")
        return

    try:
        cursor = connection.cursor()
        sql = "DELETE FROM danhmuc WHERE id = %s"
        cursor.execute(sql, (id_danhmuc,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có ID = {id_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID = {id_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối MySQL.")
