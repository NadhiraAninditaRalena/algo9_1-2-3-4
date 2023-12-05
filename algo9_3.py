print('@@@ @  @@@ @@@@   @   @ @ @@@@@@     @@@')
print('@ @ @ @  @ @   @  @   @ @ @     @   @   @')
print("@ @ @ @@@@ @  @   @@@@@ @ @@@@@@    @@@@@")
print("@ @@@ @  @ @@     @   @ @ @    @    @   @")

def hitung_hasil_kali(input_list):
    # Memastikan list tidak kosong
    if not input_list:
        return None

    # Menggunakan fungsi reduce() untuk mengalikan semua nilai dalam list
    hasil_kali = 1
    for nilai in input_list:
        hasil_kali *= nilai

    return hasil_kali

if __name__ == "__main__":
    # Masukkan list yang ingin dihitung hasil kalinya
    contoh_list = [1,2, 3, 4]

    # Memanggil fungsi hitung_hasil_kali dengan list sebagai argumen
    hasil_kali = hitung_hasil_kali(contoh_list)

    # Menampilkan hasil perhitungan hasil kali
    print("List:", contoh_list)
    print("Hasil Kali:", hasil_kali)

