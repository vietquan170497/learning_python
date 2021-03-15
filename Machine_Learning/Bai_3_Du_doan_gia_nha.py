import numpy as np 
import matplotlib.pyplot as plt

#import file mulunivariate.txt
_X = np.loadtxt('multivariate.txt', delimiter=',')
#import Theta univariate_theta.txt
Theta = np.loadtxt('multivariate_theta.txt')
#luu cot y lai
y = np.copy(_X[:,-1])
X = np.zeros((np.size(_X,0),np.size(_X,1)))
#Them cot dau bang 1
X[:,0] = 1
#Them cac cot x1->n
n = np.size(_X,1) - 1
X[:,1:] = _X[:,0:n]

#tinh loi nhuan (don vi 10000$)
predict = X@Theta
#chuyen loi nhuan ve $
predict = predict
#in cap dan so - loi nhuan dau tien 
print('%.2f feet-vuong, %d phong ngu : %.1f$' %(X[0,1],X[0,2], predict[0]))

# plot gia tri thuc the (khong lay cot bias 1 dau)
# X[:,1:] la x-axis cua bieu do khong lay cot dau
# y là y-axis, rx là red x, plot la du lieu bang dau x mau do
plt.plot(X[:,1:], y ,'rx')
# Plot du doan
plt.plot(predict/10000,y,'-b')
#ta dung don vi goc la 10000$, -b la duong thang mau xanh
#show ket quan
plt.show()











