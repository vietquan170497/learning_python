class NhanVien:
	so_thu_tu = 1
	def __init__(self, p_ten, p_que, p_diachi):
		self.ten = p_ten
		self.que = p_que
		self.diachi = p_diachi
		self.stt = NhanVien.so_thu_tu
		NhanVien.so_thu_tu += 1
	suc_manh = 50

nv_A = NhanVien("Quan dz", "ND", "HN")
nv_B = NhanVien("Quan dz", "ND", "HN")

print(nv_A.stt)
print(nv_B.stt)
print(NhanVien.so_thu_tu)