from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_to_mysql


def update_danhmuc(id_danhmuc, tenmoi, mota_moi):
    """
    Cập nhật thông tin danh mục theo ID.
    :param id_danhmuc: ID danh mục cần cập nhật
    :param tenmoi: Tên danh mục mới
    :param mota_moi: Mô tả mới
    """
    connection = connect_to_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối CSDL.")
        return

    try:
        cursor = connection.cursor()
        sql = """
            UPDATE danhmuc
            SET ten_danhmuc = %s, mo_ta = %s
            WHERE id = %s
        """
        values = (tenmoi, mota_moi, id_danhmuc)
        cursor.execute(sql, values)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục ID = {id_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục ID = {id_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối MySQL.")
