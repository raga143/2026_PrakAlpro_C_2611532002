# Buat file dengan nama multi_if1_2611532002.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: umur_2002, sim_2002
# Program ini menggunakan fungsi input()

umur_2002 = int(input("Input umur anda: "))
sim_2002 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_2002 >= 17 and sim_2002 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_2002 >= 17 and sim_2002 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_2002 < 17 and sim_2002 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_2002 < 17 and sim_2002 != 'y':
    print("Anda Belum Cukup Umur bawa motor")