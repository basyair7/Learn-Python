# Operasi pada List, Set dan String

def test1():
    # list
    contoh_list = [1, 3, 3, 5, 5, 7, 7, 9]
    print(type(contoh_list))
    print(contoh_list)
    print(len(contoh_list)) # hitung jumlah indeks yang ada di List
    
def test2():
    # Set
    contoh_list = set([1, 3, 3, 5, 5, 7, 7, 9])
    print(type(contoh_list))
    print(contoh_list)
    print(len(contoh_list))
    """
    Pada kode di atas, Anda mengonversi list menjadi set terlebih dahulu. 
    Hal ini menyebabkan anggota list berubah menjadi anggota set yang tidak memiliki duplikat. 
    Setelah itu, Anda mencetak jumlah anggota dari set. Hasilnya adalah anggota set berjumlah 5.
    """
    
def test3():
    # String
    contoh_list = "Belajar Python"
    print(type(contoh_list))
    print(contoh_list)
    print(len(contoh_list))
    
def test4():
    # min() dan max()
    angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
    print(min(angka)) # 5
    print(max(angka)) # 96
    
    # Count
    genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
    print(genap.count(6)) # 3
    
    string = "Belajar Python di Dicoding sangat menyenangkan"
    substring = "a"
    print(string.count(substring)) # 6
    
def test5():
    # In dan Not In
    kalimat = "Belajar Python di Dicoding sangat menyenangkan"
    print('Dicoding' in kalimat) # True
    print('tidak' in kalimat) # False
    print('Dicoding' not in kalimat) # False
    print('tidak' not in kalimat) # True
    
if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    x = (5, 'program', 1+3j)
    x[1] = 'Dicoding'
    print(x)
