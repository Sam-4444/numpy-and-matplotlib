import numpy as np
import matplotlib.pyplot as ml

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x=np.mean(speed)
print("mean of spead is : "+str(x))

y=np.median(speed)
print(y)

z=np.sort(speed)
print(z)
print(np.median(z))
print(np.std(z))
print(np.var(z))
print(np.percentile(z,25))

a=np.random.uniform(0,5,10)

ml.hist(a,5)
ml.show()

b=np.random.uniform(0,6,5)
print("uniform"+str(b))