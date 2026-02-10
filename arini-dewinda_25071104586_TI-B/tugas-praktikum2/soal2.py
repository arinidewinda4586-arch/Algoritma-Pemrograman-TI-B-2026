def bilangan_prima(n):
    prima = []
    
    for angka in range(2, n + 1):
        is_prima = True
        for i in range(2, int(angka ** 0.5) + 1):
            if angka % i == 0:
                is_prima = False
                break
        if is_prima:
            prima.append(angka)
    
    return prima
hasil = bilangan_prima(50)

print(hasil)
