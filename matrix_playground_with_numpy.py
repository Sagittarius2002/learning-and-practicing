import numpy as np

arr = np.zeros((6, 6), dtype = int)
print(arr)

a = np.ones((3, 3), dtype = int)
arr[0:3, 0:3] = a
print(arr)

b = np.arange(1, 7)
print(b)
i = 0
while(i < 6):
    arr[:, i] = b
    i += 1

# arr[:] = b.reshape(-1, 1) this also broadcasts b accross all columns
print(arr)

arr_reshaped = arr.reshape(3, 12)
print(arr_reshaped)

arr_sliced = arr_reshaped[0:2, 4:8]
print(arr_sliced)


c = np.eye(6, dtype = int)
print(c)
c_reshaped = c.reshape(3, 12)

arr_reshaped_new = arr_reshaped + c_reshaped

print(arr_reshaped_new)

arr_reshaped_new = arr_reshaped_new.reshape(6, 6)
d = np.ones((6, 6), dtype = int)

ar = np.vstack((arr_reshaped_new, d))
print(ar)

print(np.split(ar, 2, axis = 1))