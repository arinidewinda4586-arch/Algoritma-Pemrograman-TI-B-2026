def rata_rata(nilai):
    if len(nilai) == 0: #cek jika list kosong
        return "Data kosong"
    
    #hitung rata-rata
    return sum(nilai) / len(nilai)

#memanggil fungsi dengan list yang diberikan
data_nilai = [80, 75, 90, 60, 85]
hasil = rata_rata(data_nilai)

print(hasil)