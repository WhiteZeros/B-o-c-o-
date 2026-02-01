import numpy as np 
def heapify(arr , n , i):
    parent = i 
    left = parent * 2 + 1 
    right = parent * 2 + 2 
    if left < n and arr[left] > arr[parent]:
        parent = left
    if right < n and arr[right] > arr[parent]:
        parent = right
    if parent != i:
        arr[i] , arr[parent] = arr[parent] , arr[i]
        heapify(arr , n , parent)

def heapsort(arr: np.ndarray) -> np.ndarray:
    n = len(arr) 
    for i in range(n//2 - 1  , -1 , -1):
        heapify(arr , n , i)
    for i in range(n - 1 , 0 , -1):
        arr[0] , arr[i] = arr[i] , arr[0]
        heapify(arr , i , 0)
    return arr
