# Program untuk menampilkan pola segitiga piramida
# Nama variabel ditambah 4 digit NIM terakhir: 2002

tinggi_2002 = int(input("Masukkan tinggi segitiga: "))

for i_2002 in range(1, tinggi_2002 + 1):
    # Cetak spasi di sebelah kiri agar pola sejajar di tengah
    for j_2002 in range(tinggi_2002 - i_2002):
        print(" ", end="")
    
    # Cetak bintang beserta spasi
    for k_2002 in range(i_2002):
        print("*", end=" ")
    
    # Pindah baris
    print()