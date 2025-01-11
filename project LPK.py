def hitung_kebutuhan_gula(berat_badan, usia):
    # Menghitung kebutuhan gula harian berdasarkan berat badan dan usia
    if usia <= 3:
        kebutuhan_gula = 19  # gram per hari
    elif usia <= 8:
        kebutuhan_gula = 24  # gram per hari
    elif usia <= 18:
        kebutuhan_gula = 30  # gram per hari
    else:
        kebutuhan_gula = 36  # gram per hari

    return kebutuhan_gula

def hitung_kadar_gula_buah(jenis_buah, berat_buah):
    # Kadar gula dalam buah (gram per 100 gram buah)
    kadar_gula_buah = {
        "apel": 10,
        "pisang": 12,
        "jeruk": 9,
        "anggur": 16,
        "mangga": 14
    }

    if jenis_buah in kadar_gula_buah:
        return (kadar_gula_buah[jenis_buah] / 100) * berat_buah
    else:
        return 0

def main():
    berat_badan = float(input("Masukkan berat badan (kg): "))
    usia = int(input("Masukkan usia (tahun): "))
    jenis_buah = input("Masukkan jenis buah (apel/pisang/jeruk/anggur/mangga): ")
    berat_buah = float(input("Masukkan berat buah (gram): "))

    kebutuhan_gula = hitung_kebutuhan_gula(berat_badan, usia)
    kadar_gula = hitung_kadar_gula_buah(jenis_buah, berat_buah)

    print(f"Kebutuhan gula harian: {kebutuhan_gula} gram")
    print(f"Kadar gula dalam {berat_buah} gram {jenis_buah}: {kadar_gula} gram")

if __name__ == "__main__":
    main()
