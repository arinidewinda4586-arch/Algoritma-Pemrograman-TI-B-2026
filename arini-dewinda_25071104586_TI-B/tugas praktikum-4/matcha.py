while True:
    try:
        ukuran = input("Pilih ukuran matcha (small/medium/large): ").lower()
        
        data_kalori = {
            "small": 120,
            "medium": 180,
            "large": 250
        }
        
        if ukuran not in data_kalori:
            raise ValueError("Ukuran tidak tersedia")
        
        print("Kalori matcha:", data_kalori[ukuran], "kkal")
        break
    
    except ValueError as e:
        print("Terjadi kesalahan:", e)