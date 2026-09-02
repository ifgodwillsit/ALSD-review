def hitung_rata2(list_nilai):
    iterasi = 0
    jumlah = 0
    for i in list_nilai:
        iterasi += 1
        jumlah += i
        print(f"Nilai ke-{iterasi}: {i}")
    average = jumlah / len(list_nilai)
    print("Rata-rata:", average)
    
list_nilai = [80, 75, 90, 65, 88]
hitung_rata2(list_nilai)