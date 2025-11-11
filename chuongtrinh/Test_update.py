from common.update_danhmuc import update_danhmuc

while True:
 id = input("Mã danh mục")
 ten=input("Nhập vào tên danh mục")
 mota=input("Nhập vào mô tả")
 update_danhmuc(id,ten,mota)
 con=input("TIẾP TỤC y, THOÁT THÌ NHẤN KÝ TỰ BẤY KỲ")
 if con!="y":
     break
