import numpy as np
arr = np.array([[1, 2, 8],[3, 4, 9]])
print(arr)
print(type(arr))
print("No.of dimencion:",arr.ndim)
print("shape of array:",arr.shape)
print("size of array",arr.size)
print("Array stores element of type:", arr.dtype)
flat_arr = arr.flatten()
print("original array :\n", arr)
print("Flattened array :\n", flat_arr)
print("Adding 1 to every element:",arr+1)
arr1 = np.array([2, 4, 6, 9, 5])
print(arr1[1:5])
print(arr1[1] + arr1[2])