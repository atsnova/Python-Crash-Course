import matplotlib.pyplot as plt

x = list(range(1,1000))
y = [x_i**2 for x_i in x]
y2 = [y_i/2 for y_i in y]

#plt.plot(x,y)

plt.title("tester".title())
plt.xlabel("The value of x")
plt.ylabel("The square of x, with a another rise")

#plt.scatter(x,y2,s=35, c='x', cmap=plt.cm.Blues)


w = [1,8,27,64,125]
x = list(range(1,50000,3))
w=[x_i**3 for x_i in x]
plt.plot(x,w, cmap=cm.Hot)

plt.show()