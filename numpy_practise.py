import numpy as np

my_list = [1,2,3,4]

print(np.array(my_list))
print(type(np.array(my_list)))

print(type(my_list))

#in this arange work as simple range fuction in python
a= np.arange(0,10)

print(a)

a= np.arange(0,10,2)

print(a)

#this will print two dimetional array
#first no act as row and other act as column
print(np.zeros((5,5)))

print(np.zeros((2,5)))

#in this numbers are floats , in numpy all the integers we provide consider as float
print(np.ones((2,3)))


print(np.random.randint(0,100,(5,5)))

#from this we can  get the number for the given range with same gaps
print(np.linspace(0,10,4))
print(np.linspace(0,10,100))


np.random.seed(101)
print(np.random.randint(0,100,10))
print(np.random.randint(0,100,10))


arr1=np.random.randint(0,100,10)
print(arr1)

print(arr1.max())
print(arr1.min())

#this will produce the mean of the array
print(arr1.mean())

#thhis will produce the index of the maximum value of hte array
print(arr1.argmax())

#this will reshape the array how we define it
print(arr1.reshape(2,5))


mat = np.arange(0,100).reshape(10,10)

print(mat)

print(mat[4,6])

print(mat[:,4])

#this will produce the array with the boolean values for the given condition
print(mat%2==1)

#this will only produce the array with the values give true for the Argument
print(mat[mat>50])