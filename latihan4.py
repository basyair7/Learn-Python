# Transformasi String, dan Angka Karakter

def test1():
    # mengubah huruf kecil ke besar
    text = "dicoding"
    print(text.upper())
    print()

    # mengubah huruf besar ke kecil
    text = "DICODING"
    print(text.lower())
    print()

def test2():
    # Awalan dan akhiran
    print("Dicoding        ".rstrip()) # Metode rstrip() menghapus whitespace pada sebelah kanan atau akhir string.
    print("     Dicoding".lstrip()) # Kebalikan dari rstrip(), lstrip() bertugas untuk menghapus whitespace pada sebelah kiri atau awal string.

    # Metode startswith() bertujuan untuk menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True.
    print('Dicoding Indonesia'.startswith('Dicoding')) # true

    # Memisah dan menggabungkan string
    # .join()
    print(" ".join(['Dicoding', 'Indonesia', '!']))

    # print("123".join(['dicoding', 'indonesia']))

    # .split()
    print("Dicoding Indonesia".split("Indonesia"))
    print("""Halo
aku ikan
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.""".split('\n'))

# Pengecekan String
def test3():
    kata = "DICODING"
    print(kata.isupper()) # True
    print(kata.islower()) # False
    print(kata.isalpha()) # jika variable tidak memiliki huruf dan angka maka hasilnya True atau sebaliknya
    print(kata.isalnum()) # jika variable hanya memiliki huruf dan angka maka hasilnya True atau sebaliknya
    print('Dicoding Indonesia'.istitle()) # Metode istitle() mengembalikan nilai True jika string berisi huruf kapital pada setiap kata pertamanya.

# Formating String
def test4():
    # metode zfill
    text = 'Code'
    tambah_number = text.zfill(5)
    print(tambah_number)
    print()
    
    # metode rjust dan ljust
    text = "Dicoding"
    print(text.rjust(20, '!'))
    print(text.ljust(20, '!'))
    
    # metode center
    print("Dicoding".center(20, '-'))

if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    test4()
    
