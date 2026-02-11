from myOOP import (
    Notifikasi, Email, SMS,
    Mahasiswa,
    Produk, ProdukElektronik, ProdukMakanan
)

#tes inheritance

produk1 = Produk("Buku Tulis", 5000)
print(produk1.info_produk())

p2 = ProdukElektronik("Iphone", 9000000, 3)
print(p2.info_produk())

p3 = ProdukMakanan("Risol mayo", 7000, "2-12-2026")
print(p3.info_produk())


#polymorphism

notif1 = Notifikasi()
notif2 = Email()
notif3 = SMS()

print(notif1.kirim())
print(notif2.kirim())
print(notif3.kirim())


#encapsulation

mhs = Mahasiswa()

print(mhs.set_nilai(85))
print("Nilai mahasiswa:", mhs.get_nilai())

print(mhs.set_nilai(120))
print("Nilai mahasiswa:", mhs.get_nilai())


