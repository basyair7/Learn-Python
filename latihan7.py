# Pengenalan Aksi Sekuensial

def test1():
    print("Selamat datang dalam program Python!\n")
    print("Silakan masukkan data diri Anda.")
    nama = input("Masukkan nama Anda: ")
    tahun_lahir = input("Masukkan tahun lahir Anda: ")
    umur = 2024 - int(tahun_lahir)
    
    print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
    print("Terima kasih telah menggunakan program Python!")
    
test1()