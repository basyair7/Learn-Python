# Ternary operator

def test1():
    # result = blok_kode_jika_benar if kondisi else blok_kode_jika_salah

    lulus = True
    print("Selamat") if lulus else print("Perbaiki")
    
# Ternary Tuple
def test2():
    # (blok_kode_jika_salah, blok_kode_jika_benar)[kondisi]
    lulus = True
    result = ("Perbaiki", "Selamat")[lulus]
    print(result)
    
test2()