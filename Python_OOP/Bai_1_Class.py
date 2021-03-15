class NhanVien:
	def __init__(self, p_ten, p_que, p_diachi):
		self.ten = p_ten
		self.que = p_que
		self.diachi = p_diachi

	def xinchao(self):
		return "Xin chao, toi la: " + self.ten

# nv_A = NhanVien()
# nv_A.ten = "QuanNV"
# nv_A.nhanvien = "dep trai"

nv_A = NhanVien("Quan dz", "ND", "HN")

# print(nv_A.ten)		
# print(nv_A.que)
# print(nv_A.diachi)

print(nv_A.xinchao())
