import numpy as np 
import Sort as s

def Sinhtest(lim):
    test_interger = []
    for i in range(5):
        test_interger.append(np.random.randint(0, lim, size= lim))
    test_interger[0] = s.sort_numpy(test_interger[0])
    test_interger[1] = s.sort_numpy(test_interger[1])[::-1]

    test_float = []
    for i in range(5):
        test_float.append(np.random.uniform(0, lim, size= lim))
    test_float[0] = s.sort_numpy(test_float[0])
    test_float[1] = s.sort_numpy(test_float[1])[::-1]
    return [test_interger , test_float]
