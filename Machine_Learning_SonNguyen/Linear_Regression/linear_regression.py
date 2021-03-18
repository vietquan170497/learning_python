import pandas as pd 
import matplotlib.pyplot as plt


dataframe = pd.read_csv('Advertising.csv', header=5)

# print(dataframe)
X = dataframe.values[:,2]
y = dataframe.values[:,4]

# plt.scatter(X,y,marker='o')
# plt.show()

def predict(feature, weight, bias):
	return weight*feature + bias

def cost_function(X,y,weight,bias):
	n = len(X)
	sum_error = 0
	for i in range(n):
		sum_error += (y[i] - (weight*X[i] + bias))**2
	return sum_error/n

def update_weight (X,y,weight,bias,learning_rate):
	n = len(X)
	weight_temp = 0.0
	bias_temp = 0.0
	for i in range(n):
		weight_temp += -2*X[i]*(y[i]-(X[i]*weight + bias))
		bias_temp += -2*(y[i]-(X[i]*weight + bias))
	weight -= (weight_temp/n)*learning_rate
	bias -= (bias/n)*learning_rate

	return weight, bias

def train(X,y,weight,bias,learning_rate,iter): #iten so lan lap
	cost_his = []
	for i in range(iter):
		weight, bias = update_weight(X,y,weight,bias,learning_rate)
		cost = cost_function(X,y,weight,bias)	
		cost_his.append(cost)
	return weight, bias, cost_his

weight, bias, cost = train(X,y,0.03,0.0014,0.001,30)

print(weight)
print(bias)
print(cost)
print("Du doan: ")
print(predict(19, weight, bias))

solanlap = [ i for i in range(30)]
plt.plot(solanlap,cost)
plt.show()
