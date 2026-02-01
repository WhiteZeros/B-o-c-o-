import time 
import numpy as np
from Heapsort import heapsort as hs  
from Quicksort import quicksort as qs 
from Mergesort import merge_sort as ms
from Sort import sort_numpy as s
import Sinhtest as gen 
import pandas as pd 


#time run of sort function 
def time_run(func , arr):
    start = time.time()
    arr = func(arr)
    end = time.time() 
    return end - start

#Create test 
test = gen.Sinhtest(lim = 1000000)
    #test[0] is interger 
    #test[1] is float 

#Build chart 
Type = ["SO NGUYEN" , "SO THUC"]

#array function sort 
func = [hs , qs , ms , s]


Head = ['Test' ,'Heap sort(s)' , 'Quick sort(s)' , 'Merge sort(s)' , 'Sort numpy(s)']
for i in range(0 , 2):
    Data = {h : [] for h in Head}
    Data['Test'] = [i + 1 for i in range(5)]
    for j in range(4):
        for th in test[i]:
            Data[Head[j + 1]].append(time_run(func[j] , th))
    
    df = pd.DataFrame(Data)
    df.to_excel(f"BANG THONG KE VOI DU LIEU {Type[i]}.xlsx", index=False)




