# Data Type

# list
x = [1, 2.2, 'Dicoding', True]
print(type(x))
print(x[3])

# tuple
x = (1, "Dicoding", 1+3j)
print(type(x))
print(x[1])

# Set
# Set yaitu kumpulan item bersifat unik, tanpa urutan dan dapat diinisialisasikan dengan kurawal
# Set tidak sama seperti list maupun tuple yang bisa melakukan indeksing karena set tidak memiliki indeks
x = {1, 2, 7, 2, 3, 13, 3}
print(type(x))
print(x)

# Dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(type(x))
print(x['name'])