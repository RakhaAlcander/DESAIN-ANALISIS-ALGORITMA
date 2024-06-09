def penukaran_uang_greedy(jumlah_uang):
    uang_koin = [1000, 500, 200, 100]
    jumlah_koin = [0, 0, 0, 0]

    for i in range(len(uang_koin)):
        while jumlah_uang >= uang_koin[i]:
            jumlah_koin[i] += 1
            jumlah_uang -= uang_koin[i]

    return jumlah_koin
uang_koin = [1000, 500, 200, 100]
jumlah_koin = [0, 0, 0, 0]
jumlah_uang = int(input("Masukkan jumlah uang Rupiah: "))
hasil_penukaran = penukaran_uang_greedy(jumlah_uang)

print("Hasil penukaran:")
for i in range(len(hasil_penukaran)):
    if hasil_penukaran[i] > 0:
        print(f"{uang_koin[i]} Rupiah: {hasil_penukaran[i]} koin")
