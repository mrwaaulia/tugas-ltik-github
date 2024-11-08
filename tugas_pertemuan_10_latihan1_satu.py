"""
Nama: Marwa Aulia Lukman
NIM: 2403029
Kelas: 1B
"""

def fibonacci(n):
    a, b = 0, 1
    count = 0
    
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

jumlah_deret = int(input("Masukkan jumlah angka Fibonacci yang ingin ditampilkan: "))
fibonacci(jumlah_deret)

