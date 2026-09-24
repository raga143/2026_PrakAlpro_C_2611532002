# Buat file dengan nama if_elif_else1_2611532002.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: umur_2002, sim_2002
# Program ini menggunakan fungsi input()

umur_2002 = int(input("Input umur anda: "))
sim_2002 = input("Apakah Anda Sudah Punya Sim C: ")[0]

if umur_2002 >= 17 and sim_2002 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")
elif umur_2002 >= 17 and sim_2002 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2002 < 17 and sim_2002 == 'y':
    print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur dan tidak boleh bawa motor")
    print("program selesai")
