# fundamental matriks

import numpy
import sys

def test1():
    matriks = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for i in range(1, 3):
        for j in range(1, 3):
            matriks[i][j] = i,j
            
    print(matriks)
    
def test2():
    matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
    print(matriks)
    
def test3():
    var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

    print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
    print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)
    
test3()