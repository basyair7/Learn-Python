# Looping (Perulangan)

def test1():
    var_list = [1,2,3,4,5,6,7,8,9,10]
    for i in var_list:
        print(i, end=' ')

def test2():
    # for i in range(start, stop, step)
    # "Step" merupakan nilai penambahan 
    # antara setiap dua bilangan dalam urutan yang bersifat opsional. Jika nilai tersebut tidak diberikan, 
    # secara default nilai yang dimasukkan adalah 1.
    for i in range(1, 10, 2):
        print(i, end=" ")

def test3():
    counter = 1
    while counter <= 5:
        print(counter, end=" ")
        counter += 1
        
# For bersarang
def test4():
    for i in range(1, 3):  # outer loop
        for j in range(1, 3): # inner loop
            print(f"outler={i}, inner={j}")
            
def test5():
    for i in range(2):
        print("Perulangan luar (outer): ",i)
        for j in range(10):
            print("Perulangan dalam (inner): ",j)
            if j == 1: break
            
def test6():
    huruf = []
    for i in "Dico ding":
        if i == ' ':
            continue
        
        huruf.append(i)
        
    print(f"Huruf saat ini adalah : {huruf}")

def test7():
    numbers = [1, 2, 3, 4, 5]
    for i in numbers:
        if i == 6:
            print("Ada angka 6")
            break
    else:
        print("Tidak ada angka 6")
        
# else setelah while
def test8():
    count = 0
    while(count < 3):
        print("Dicoding indonesia")
        count += 1
    else:
        print("Blok else dieksekusi karena kondisi pada while salah (3 < 3 == False)")

if(__name__ == "__main__"):
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    i = 9 
    if i<10:    
        print(i) 
    pass