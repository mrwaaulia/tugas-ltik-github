"""
Nama: Marwa Aulia Lukman
NIM: 2403029
Kelas: 1B
"""

def funcArgs(*angka):
    print(f"Angka yang dimasukkan yaitu: {angka}")
    jumlah = sum(angka)
    rataRata = jumlah / len(angka)   
    print(f"Hasil penjumlahan: {jumlah}")
    print(f"Rata-rata: {rataRata}")
    return jumlah, rataRata

# Menggunakan loop untuk mengumpulkan beberapa angka dari user input
angka_list = []
while True:
    angka_input = input("Masukkan angka : ")
    if angka_input == "":
        print("Anda selesai menginputkan angka")
        break
    elif angka_input.isdigit():  # Memastikan input adalah angka
        angka_list.append(int(angka_input))

# Memanggil fungsi dengan angka yang telah dimasukkan user input
funcArgs(*angka_list)

