# Implementasi Matriks di Python
# Deklarasi Matriks

import numpy as np

def test1():
    matriks = [[0 for i in range(4)] for i in range(3)]
    print(matriks)

def test2():
    matriks = [[0 for i in range(3)] for j in range(3)]
    nilai = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    
    for i in range(3):
        for j in range(3):
            matriks[i][j] = nilai[i][j]
            
    print(matriks)

def test3():
    var_mat = [[5,0], [1, -2]]
    def_mat = [[0 for j in range(2)] for i in range(2)]
    
    
    for i in range(2):
        for j in range(2):
            def_mat[i][j] = var_mat[i][j]*2 
            
    print(def_mat)
    
def test4():
    var_mat = np.array([[5,0], [1, -2]])
    result = var_mat*2
    print(result)
    
test4()