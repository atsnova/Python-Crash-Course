import random


def RandStep(step_hor,step_ver,steps):
    step_hor =[]
    step_ver = []
    i=0
    while i < steps:
 #       prob_step = round(np.random.uniform(0,1))
 #       prob_magnitude_hor = round(np.random.uniform(-5,5),0)
 #       prob_magnitude_ver = round(np.random.uniform(-5,5),0)
 
#        prob_step = round(np.random.normal(0,0.25))
 #       prob_magnitude_hor = round(np.random.normal(0,1),0)
 #       prob_magnitude_ver = round(np.random.normal(0,1),0)


        prob_step=random.randint(-1,1)
        prob_magnitude_hor = random.randint(0,4)
        prob_magnitude_ver = random.randint(0,4)


        if i==0: 
            step_hor.append(prob_step*prob_magnitude_hor)
            step_ver.append(prob_step*prob_magnitude_ver)
        else:
            step_hor.append(step_hor[-1]+prob_step*prob_magnitude_hor)
            step_ver.append(step_ver[-1]+prob_step*prob_magnitude_ver)
            print(i-1)
            print(step_hor[-1])
           # print(step_hor[i])
            # step_hor.append(step_hor[i]+prob_step*prob_magnitude_hor)
           # step_ver.append(step_ver[i]+prob_step*prob_magnitude_ver)

        

        i=i+1



 #   print(prob_step)
 #   print(prob_magnitude_hor)
 #   print(prob_magnitude_ver)
 #   print(step_hor)
 #   print(step_ver)

    return step_hor, step_ver


#define number of steps
steps = int(input("Enter the number of steps to attempt: "))
x,y = (RandStep("x","y",steps))
print(x)
print(y)


import matplotlib.pyplot as plt
#plt.scatter(x,y)

point_numbers = list(range(steps))

plt.scatter(x, y, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
plt.scatter(x[0], y[0], c='green', edgecolors='none', s=100)
plt.scatter(x[-1], y[-1], c='red', edgecolors='none',s=100)


plt.show()