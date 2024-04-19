# definisi subprogram
"""Fungsi adalah blok kode yang dapat menerima input, melakukan pemrosesan, dan mengembalikan output. 
Hasil atau output tersebut dinyatakan dalam sebuah tipe data yang eksplisit. 
Artinya, fungsi yang dibuat dapat ditentukan untuk mengembalikan tipe data integer, string, atau lainnya."""
"""Prosedur adalah deretan instruksi yang jelas keadaan awal (initial state) dan keadaan akhirnya (final state). 
Prosedur mirip dengan program secara umum, tetapi memiliki cakupan yang kecil dan terbatas."""

def volume_persegi(panjang, lebar, tinggi):
    return panjang*lebar*tinggi


def test1():
    p = 4
    l = 4
    t = 4
    v = volume_persegi(p,l,t)
    print(f"Volume persegi dengan p={p} cm, l={l} cm, dan t={t} cm adalah {v} cm^3")
    
test1()