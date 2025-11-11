import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

from ketnoidb.ketnoi_mysql import connect_to_mysql


# ------------------------------

# ------------------------------
# HÀM HIỂN THỊ DỮ LIỆU
# ------------------------------
def load_data():
    for item in tree.get_children():
        tree.delete(item)

    conn = connect_to_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, ten_danhmuc, mo_ta FROM danhmuc")
        for row in cursor.fetchall():
            tree.insert('', tk.END, values=row)
        cursor.close()
        conn.close()


# ------------------------------
# HÀM THÊM DANH MỤC
# ------------------------------
def add_danhmuc():
    ten = entry_ten.get()
    mota = entry_mota.get()
    if ten == "":
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên danh mục!")
        return
    conn = connect_to_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)", (ten, mota))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Thành công", "Đã thêm danh mục mới!")
        load_data()
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)


# ------------------------------
# HÀM XÓA DANH MỤC
# ------------------------------
def delete_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chọn hàng", "Vui lòng chọn danh mục cần xóa.")
        return
    item = tree.item(selected[0])
    id_danhmuc = item['values'][0]

    conn = connect_to_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM danhmuc WHERE id = %s", (id_danhmuc,))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Đã xóa", f"Đã xóa danh mục ID = {id_danhmuc}")
        load_data()


# ------------------------------
# HÀM CẬP NHẬT DANH MỤC
# ------------------------------
def update_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chọn hàng", "Vui lòng chọn danh mục cần sửa.")
        return

    id_danhmuc = tree.item(selected[0])['values'][0]
    ten_moi = entry_ten.get()
    mota_moi = entry_mota.get()

    if ten_moi == "":
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên danh mục!")
        return

    conn = connect_to_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE danhmuc SET ten_danhmuc = %s, mo_ta = %s WHERE id = %s",
                       (ten_moi, mota_moi, id_danhmuc))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Thành công", f"Đã cập nhật danh mục ID = {id_danhmuc}")
        load_data()


# ------------------------------
# HÀM KHI CHỌN DÒNG TRONG TREEVIEW
# ------------------------------
def select_item(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
        entry_ten.insert(0, item['values'][1])
        entry_mota.insert(0, item['values'][2])


# ------------------------------
# GIAO DIỆN CHÍNH
# ------------------------------
root = tk.Tk()
root.title("Quản lý danh mục")
root.geometry("600x400")
root.resizable(False, False)

# Frame nhập
frame_input = tk.Frame(root, pady=10)
frame_input.pack()

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, padx=5)
entry_ten = tk.Entry(frame_input, width=30)
entry_ten.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, padx=5)
entry_mota = tk.Entry(frame_input, width=30)
entry_mota.grid(row=1, column=1, padx=5)

# Frame nút bấm
frame_buttons = tk.Frame(root, pady=10)
frame_buttons.pack()

tk.Button(frame_buttons, text="Thêm", command=add_danhmuc, width=10, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Sửa", command=update_danhmuc, width=10, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Xóa", command=delete_danhmuc, width=10, bg="#f44336", fg="white").grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Tải lại", command=load_data, width=10, bg="#9C27B0", fg="white").grid(row=0, column=3, padx=5)

# Bảng hiển thị
columns = ("id", "ten", "mota")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.heading("id", text="ID")
tree.heading("ten", text="Tên danh mục")
tree.heading("mota", text="Mô tả")
tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<<TreeviewSelect>>", select_item)

# Khởi tạo dữ liệu
load_data()

root.mainloop()
