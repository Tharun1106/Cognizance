import numpy as np
a = np.random.randint(0,2,6)
print("The first array is : " , a)
b = np.random.randint(0,2,6)
print("The second array is : " , b)
c = np.allclose(a, b)
if (c == True):
    print("Both the arrays are equal.")
    print("Therefore : ", c)
else:
    print("Both the arrays are not equal.")
    print("Therefore : ", c)
