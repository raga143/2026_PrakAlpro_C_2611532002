# Buat file dengan nama nested_for4_2611532002.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_2002
# Program ini menggunakan fungsi input()

tinggi_2002 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2002 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2002 = tinggi_2002
    c_2002 = a_2002
    lebar_2002 = (2 * tinggi_2002) - 2

    for i_2002 in range(1, tinggi_2002 + 1):
        b_2002 = c_2002 + 1

        for j_2002 in range(1, lebar_2002 + 1):

            # Baris atas dan bawah
            if i_2002 == 1 or i_2002 == tinggi_2002:
                if j_2002 == 1 or j_2002 == lebar_2002:
                    print("*", end="")
                else:
                    print("-", end="")

            # Baris isi
            else:
                if j_2002 == 1 or j_2002 == lebar_2002:
                    print("|", end="")
                else:
                    if j_2002 == c_2002:
                        print("<", end="")
                    elif j_2002 == b_2002: 
                        print(">", end="")
                    elif j_2002 == (lebar_2002 - c_2002):
                        print("<", end="")
                    elif j_2002 == (lebar_2002 - c_2002 + 1):
                        print(">", end="")
                    elif j_2002 > b_2002 and j_2002 < (lebar_2002 - c_2002):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_2002 -= 2

        if a_2002 <= 0:
            c_2002 = (-a_2002) + 2
        else:
            c_2002 = a_2002