import numpy as np 
import matplotlib.pyplot as plt

# A = np.loadtxt('univariate.txt', delimiter=',')
# print(A[0:4,:])
# np.savetxt('univariate_save.txt',A,fmt='%.2f',delimiter=',')

#import file univariate.txt
X = np.loadtxt('univariate.txt', delimiter=',')
#import Theta univariate_theta.txt
Theta = np.loadtxt('univariate_theta.txt')
#luu cot y lai
y=np.copy(X[:,-1])
#chuyen cot dau tien sang cot 2
X[:,1] = X[:,0]
#chuyen cot dau tien = 1
X[:,0] = 1
#tinh loi nhuan (don vi 10000$)
predict = X@Theta
#chuyen loi nhuan ve $
predict = predict*10000
#in cap dan so - loi nhuan dau tien 
print('%d nguoi: %.2f' %(X[0,1]*10000, predict[0]))

# plot gia tri thuc the (khong lay cot bias 1 dau)
# X[:,1:] la x-axis cua bieu do khong lay cot dau
# y là y-axis, rx là red x, plot la du lieu bang dau x mau do
plt.plot(X[:,1:], y ,'rx')
# Plot du doan
plt.plot(predict/10000,y,'-b')
#ta dung don vi goc la 10000$, -b la duong thang mau xanh
#show ket quan
plt.show()











