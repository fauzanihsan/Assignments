import matplotlib.pyplot as plt
import math

initial_velocity = int(input("Input the initial velocity:"))
angle = int(input("Input the angle:"))

velocity_x = math.cos(math.radians(angle))*initial_velocity
velocity_y = math.sin(math.radians(angle))*initial_velocity
time = 2*initial_velocity*math.sin(math.radians(angle))/10

x =[]
y =[]

for i in range(0, int(time)+1):
    x_axis = velocity_x*i
    x.append(x_axis)

for i in range(0, int(time)+1):
    y_axis = (velocity_y*i)-(1/2*10*i**2)
    y.append(y_axis)


print(x)
print(y)
plt.plot(x,y)
plt.show()
