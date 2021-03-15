class NhanVien:
	luong = 50
	def __init__(self, p_ten, p_que, p_diachi):
		self.ten = p_ten
		self.que = p_que
		self.diachi = p_diachi

class NhanVienSMV(NhanVien):
	luong = 40
	def __init__(self, p_ten, p_que, p_diachi, p_tuoi):
		# self.ten = p_ten
		# self.que = p_que
		# self.diachi = p_diachi
		# self.tuoi = p_tuoi

		super().__init__(p_ten, p_que, p_diachi)
		self.tuoi = p_tuoi

nv_A = NhanVienSMV("Quan dz", "ND", "HN", "25")
print(nv_A.__dict__)
print(nv_A.luong)