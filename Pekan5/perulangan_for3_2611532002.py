# Buat file dengan nama perulangan_for3_1018.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1018
# Program ini menggunakan fungsi input()

ulang_2002 = int(input("Masukkan jumlah perulangan: "))

jumlah_2002 = 0
for i_2002 in range(1, ulang_2002 + 1):
    print(i_2002, end=" ")
    jumlah_2002 = jumlah_2002 + i_2002

    if i_2002 < ulang_2002:
        print("+ ", end="")
    else:
        print(" = ", jumlah_2002, end="")
        
print()
print("Jumlah = ", jumlah_2002)