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
        # Sửa lỗi: Thêm câu lệnh SQL và logic xử lý
        sql = "DELETE FROM danhmuc WHERE id_danhmuc = %s"
        cursor = connection.cursor()

        cursor.execute(sql, (id_danhmuc,))
        connection.commit()

        print(f"Danh mục có ID {id_danhmuc} đã được xóa thành công.")

    except Error as e:
        print(f"Lỗi khi xóa danh mục: {e}")
        connection.rollback()

    finally:
        connection.close()
