# In tiêu đề phần mềm trong khung hình chữ nhật
print("+-------------------------------+")
print("| PHẦN MỀM XẾP LOẠI HỌC SINH    |")
print("+-------------------------------+")

# Nhập họ tên
ho_ten = input("Nhập vào họ tên: ")

# Nhập điểm các môn
diem_toan = float(input("Nhập vào điểm môn Toán: "))
diem_van = float(input("Nhập vào điểm môn Văn: "))
diem_anh = float(input("Nhập vào điểm môn Anh: "))

# Tính điểm trung bình
diem_trung_binh = (diem_toan + diem_van + diem_anh) / 3

# Xuất kết quả
print(f"Học sinh {ho_ten} đạt điểm trung bình các môn là: {diem_trung_binh:.2f}")
