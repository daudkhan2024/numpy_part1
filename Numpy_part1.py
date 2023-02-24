from timeit import timeit

import numpy as np
a =np.array([1,2,3,4,5,6])
print(a[0])
b = np.array([[1,2,3,],[2,3,4,]])
print(b[0])

# Creating Basic array
x = np.array([1,2,3,4])
print(x)
#in arry there is no comma
# #while in list there is comma
y = [1,2,3,4]
print(y)


#checking datatype
print(type(x))
print(type(y))

#USES OF ARRAY
'''#numpy use  in mathematical operations on arrays
# its fast consume less memory
#logical,mathematical ,shape manipulation ,sorting
#linear algebra and much more can be use in array'''

# Check speed of Numpy %timeit function
# to check how much total time will take in executing
# a program we use %%timeit

#Numpy Array Creation
# Creating Basic array
x = np.array([1,2,3,4])
print(x)

#now i will make alist and convert into array
x1 = [12,4,5,6]
y1 = np.array(x1)
print(y)

print(type(y1))



l = []
for i in range(1,5):
    int_1 = int(input("enter :"))# if we do not make it int it will show str
    l.append(int_1)

print(np.array(l))


# one dimension array will be with one bracket[]
# two dimension array will be with two [[]]
#three dimension array will be three [[[]]]
# for higher dimensional arrays we use ndim to check

x = np.array([1,2,3,4])
print(x)
print
print(x.ndim)  # it will show the array is one dimension

y = np.array([[1,2,3],[33,4,5]])
print(y.ndim)# it will show the dimension is 2

ar2 =np.array ([[9,8,7],[6,5,4]])
print(ar2.ndim)
print(ar2)  # it will show you inform of matrix

# To make three by three matrix
ar3 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(ar3)
print(ar3.ndim)

# To Create 10 dimension array ,,,shortcut way
arn = np.array([1,2,3],ndmin = 10)
print(arn)
print(arn.ndim)

