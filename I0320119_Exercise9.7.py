import array
# mengonversi string ke dalam array.array

B = array.array('b')
B.fromstring("Python")

# fromstring sudah tidak tersedia pada Python3.9

for karakter in B:
    print("%c " % karakter, end='')