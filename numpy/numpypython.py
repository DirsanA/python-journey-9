import numpy as np

arr=[1.2,3.5,6.7]

arr=np.array(arr,dtype='float32')

copy_arr=arr.copy()

arr[0]=12.4

print(arr)
