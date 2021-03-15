# Class Method

# class NhanVien:
# 	luong = 50
# 	def __init__(self, p_ten, p_que, p_diachi):
# 		self.ten = p_ten
# 		self.que = p_que
# 		self.diachi = p_diachi
#
# 	@classmethod
# 	def from_string(cls, s):	
# 		lst = s.split('-');
# 		new_lst = [st.strip() for st in lst]
# 		ten, que, diachi = new_lst
# 		return cls(ten,que,diachi)

# nv_str = "QuanNV dz - ND - HN"
# nv_A = NhanVien.from_string(nv_str);
# print (nv_A.__dict__)

# -------------
# Static Method
class NhanVien:
	luong = 50
	def __init__(self, p_ten, p_que, p_diachi):
		self.ten = p_ten
		self.que = p_que
		self.diachi = p_diachi

	@staticmethod
	def print_infor():
		print("Thong tin nhan vien")

nv_A = NhanVien("QuanNV dz", "ND", "HN")
nv_A.print_infor()
