import numpy as np 

#ADD matrix
# _A = [[1,2,3],[4,5,6]]
# _B = [[2,3,4],[7,9,21]]

# A =np.array(_A)
# B =np.array(_B)

# print(A)
# # print(_A)
# # print("A[0,1] : ",A[0,1])
# # print("A[:,1] : ",A[:,1])
# # print("A[1,:] : ",A[1,:])
# print("A + B = \n",A+B)
# print("A - B = \n",A-B)

# ----------------
#MUL matrix
# _A = [[1,2,3],[4,5,6],[7,8,9]]
# _B = [[1,2],[4,5],[6,7]]
# A = np.array(_A)
# B = np.array(_B)
# print("A * B = \n",A.dot(B))
# print("A * B = \n",A@B)

# ----------------
# Ma tran don vi
# A = np.eye(5)
# print(A)

# ----------------
#Nhan 2 ma tran
# _A = [[1,2,3],[4,5,6]]
# _B = [[1,2,3],[4,5,6]]
# A = np.array(_A)
# B = np.array(_B)
# print(A*B)

# ----------------
#Ma tran dao
# _A = [[1,2,3],[4,5,6],[7,8,9]]
# A = np.array(_A)
# A_i = np.linalg.pinv(A)
# print(A_i)
# print(A_i@A)

# ----------------
#Ma tran chuyen vi
_A = [[1,2,3],[4,5,6]]
A = np.array(_A)
A_i = np.transpose(A)
print(A_i)
print(A)
print(A[:,-1])


