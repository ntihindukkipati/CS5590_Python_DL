import numpy as np
x=np.random.randint(1,20,15,int)  #used for inserting random variable from 1-20 into 15 size array
x=x.reshape((3,5))
y=x.reshape((3,5))
print(x)
x=np.where(x==np.amax(x,axis=1).reshape(-1,1),0,x)  #given a condition to change max value of a row to 0
print(x)