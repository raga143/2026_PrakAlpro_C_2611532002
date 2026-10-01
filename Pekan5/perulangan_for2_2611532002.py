# Buat file dengan nama perulangan_for2_2611532002.py
# Buatlah program untuk perulangan for dalam python
# Nama Variabel ditambah 4 digit nim terakhir contoh: ulang_2002
# Program ini menggunakan fungsi input()

ulang_2002 = int(input("Masukkan jumlah perulangan: "))

jumlah = 0
for i in range(1, ulang_2002 + 1):
    print(i,end=" ")
    jumlah += i

if i < ulang_2002:
    print(" + ",end="")
else:
    print(" = ", jumlah, end="")
print()
print("jumlah =", jumlah)