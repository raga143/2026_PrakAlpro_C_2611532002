print("===SELAMAT DATANG DI WAHANA REKREASI DEPARTEMEN INFORMATIKA===")

nama_pengunjung_2002 = input("Silahkan masukkan nama anda: ")
umur_2002 = int(input("Silahkan masukkan umur anda: "))

ktp_2002 = input("Apakah anda punya KTP (y/t): ") .strip() .lower() [0]



print("===SELAMAT DATANG KE LOKET PEMBAYARAN WAHANA")
print("Paket Wahana yang Tersedia (1-5):")
print("""
      1. Wahana Safari Rimba | Harga Satuan: Rp 50.000
      2. Wahana Arung Jeram | Harga Satuan: Rp 75.000
      3. Wahana Motor ATV Ekstrim | Harga Satuan: Rp 120.000
      4. Wahana Roller Coaster Kilat | Harga Satuan: Rp 100.000
      5. Wahana All-Access VIP | Harga Satuan: Rp 220.000
      """)

wahana_2002 = int(input("Silahkan Masukkan Wahana yang anda pilih: "))
jumlah_tiket_2002 = int(input("Masukkan Jumlahkan tiket yang ingin anda beli: ")) 
if jumlah_tiket_2002 <=0:
    print("Jumlah Tiket yang anda masukkan tidak valid")
    exit()
    

harga_2002 = 0

print("\n---KELAYAKAN PENGENDARA WAHANA---")

match wahana_2002:
    case 1:
        if umur_2002 >= 15:
            print("\nSilahkan Memasukki Wahana")
        else:
            print("Mohon membawa Pendamping Anda")
            exit()
        harga_2002 = 50000
    
    case 2:
        if umur_2002 >=16:
            print("\nSilahkan Memasukki Wahana")
        else:
            print("Mohon Membawa Pendamping Anda")
            exit()
        harga_2002 = 75000
    
    case 3:
        if umur_2002 >= 18 or ktp_2002=='y':
            print("\nSilahkan Memasukki Wahana")
        elif umur_2002 >=15:
            print("Mohon Membawa Pendamping Anda")
        else:
            print("Silahkan Pilih Wahana yang sesuai dengan umur anda")
            exit()
        harga_2002 = 120000
            
    case 4:
        if umur_2002 >= 17 and ktp_2002=='y':
            print("\nSilahkan Memasukki Wahana")
        else:
            print("Mohon Bawa Pendamping Anda ")
        harga_2002 = 100000
        
    case 5:
        if umur_2002 >= 18 and ktp_2002=='y':
            print("\nSilahkan Memasukki Wahana")
        else:
            print("Mohon Membawa Pendamping Anda")
            exit()
        harga_2002 = 220000 
        
    case _:
        print("\nMohon Pilih sesuai yang ada di list yang kami sediakan") 
        exit()
        
        
nominal_pembayaran_2002 = harga_2002*jumlah_tiket_2002
promo_2002 = input("Apakah kode promo yang anda miliki valid (y/t): ") .strip() .lower() [0]
diskon_2002 = 0
member_2002 = input("Apakah anda merupakan member(y/t):") .strip() .lower() [0]
if nominal_pembayaran_2002 >= 2300000:
   diskon_2002 +=10

if member_2002 == 'y':
    diskon_2002 +=5

if promo_2002 == 'y':
    diskon_2002 +=15

diskon_keseluruhan_2002 = nominal_pembayaran_2002 * (diskon_2002/100)
total_bayar_2002 = nominal_pembayaran_2002 - diskon_keseluruhan_2002
    
print("\n---Rincian Pembayaran---")
print(f"Subtotal: Rp{nominal_pembayaran_2002 :,.0f}")
print(f"Total Diskon: {diskon_2002}% (Rp{diskon_keseluruhan_2002 :,.0f})")
print(f"Total Pembayaran: Rp{total_bayar_2002 :,.0f}")
print("Terima Kasih Atas Kunjungan Anda")
print("Kami Nantikan Kunjungan Anda yang Berikutnya")
