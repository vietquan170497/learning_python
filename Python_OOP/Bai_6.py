# class NhanVien:
# 	luong = 50
# 	def __init__(self, p_ten, p_que):
# 		self.ten = p_ten
# 		self.que = p_que
# 		self.diachi = p_ten + " - " + p_que

# 	def print_infor(self):
# 		return '{} {}'.format(self.ten, self.que)
# 	def diachis(self):
# 		return '{} depzai {}'.format(self.ten, self.que)

# nv_A = NhanVien("Quan dz", "ND")
# nv_A.ten = "QuanNV"
# nv_A.que = "Vu Ban"

# print(nv_A.ten)
# print(nv_A.que)
# print(nv_A.diachis())
# print(nv_A.print_infor())

# -------------------
# getter
# class NhanVien:
# 	luong = 50
# 	def __init__(self, p_ten, p_que):
# 		self.ten = p_ten
# 		self.que = p_que

# 	@property	
# 	def print_infor(self):
# 		return '{} {}'.format(self.ten, self.que)

# 	@property
# 	def diachi(self):
# 		return '{} depzai {}'.format(self.ten, self.que)

# nv_A = NhanVien("Quan dz", "ND")
# nv_A.ten = "QuanNV"
# nv_A.que = "Vu Ban"

# print(nv_A.ten)
# print(nv_A.que)
# print(nv_A.diachi)
# print(nv_A.print_infor)

# -------------------
#setter
# class NhanVien:
# 	def __init__(self, p_ten, p_que):
# 		self.ten = p_ten
# 		self.que = p_que

# 	@property	
# 	def print_infor(self):
# 		return '{} {}'.format(self.ten, self.que)

# 	@property
# 	def diachi(self):
# 		return '{} depzai {}'.format(self.ten, self.que)

# 	@print_infor.setter
# 	def print_infor(self,dia_chi_moi):
# 		ten_moi, que_moi = dia_chi_moi.split(' ')
# 		self.ten = ten_moi
# 		self.que = que_moi

# nv_A = NhanVien("Quan dz", "ND")
# nv_A.print_infor = "QuanNV VuBan"
# print(nv_A.print_infor)

# -------------------
#deleter
class NhanVien:
	def __init__(self, p_ten, p_que):
		self.ten = p_ten
		self.que = p_que

	@property	
	def print_infor(self):
		return '{} {}'.format(self.ten, self.que)

	@property
	def diachi(self):
		return '{} depzai {}'.format(self.ten, self.que)
	
	@print_infor.setter
	def print_infor(self,dia_chi_moi):
		ten_moi, que_moi = dia_chi_moi.split(' ')
		self.ten = ten_moi
		self.que = que_moi

	@print_infor.deleter
	def print_infor(self):
		self.ten = None
		self.que = None
		print("Da xoa")

nv_A = NhanVien("Quan dz", "ND")
nv_A.print_infor = "QuanNV VuBan"
print(nv_A.print_infor)

del nv_A.print_infor
print(nv_A.print_infor)