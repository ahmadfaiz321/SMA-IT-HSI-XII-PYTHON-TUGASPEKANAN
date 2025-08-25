
#kasir cerdas 2.0-edisi functions&loops


from ast import Continue


def tampilkan_header():
    print("Fungsi tampilkan_header dipanggil")
def hitung_subtotal(daftar_harga, daftar_jumlah):
    print("Fungsi hitung_subtotal dipanggil")
    return 0  # sementara return 0
def hitung_diskon(subtotal):
    print("Fungsi hitung_diskon dipanggil")
    return 0, 0  # sementara return diskon = 0 dan persen_diskon = 0
def tampilkan_struk(semua_nama, semua_harga, semua_jumlah, subtotal, total_diskon, persen_diskon):
    print("Fungsi tampilkan_struk dipanggil")
daftar_nama_barang = []
daftar_harga_barang = []
daftar_jumlah_barang = []
def tampilkan_header():
    print("============================================")
    print("     SELAMAT DATANG DI TOKO SERBAGUNA")
    print("============================================")

    tampilkan_header()
    print("--- Masukkan Detail Barang ---")
print("(Ketik 'selesai' di nama barang untuk selesai)")

while True:
    nama_barang = input("Nama Barang: ")
    if nama_barang.lower() == "selesai":
        break
try:
    harga = float(input("Harga Satuan: Rp "))
    jumlah = int(input("Jumlah: "))
except ValueError:
     print("Input tidak valid. Harus angka untuk harga dan jumlah.")
     Continue
daftar_nama_barang.append(nama_barang)
daftar_harga_barang.append(harga)
print("--- Barang berhasil ditambahkan! ---")

def hitung_subtotal(daftar_harga, daftar_jumlah):
    total = 0
    for i in range(len(daftar_harga)):
        total += daftar_harga[i] * daftar_jumlah[i]
    return total
def hitung_diskon(subtotal):
    if subtotal >= 500000:
        persen_diskon = 10
    elif subtotal >= 300000:
        persen_diskon = 5
    else:
        persen_diskon = 0

    jumlah_diskon = subtotal * persen_diskon / 100
    return jumlah_diskon, persen_diskon
def tampilkan_struk(semua_nama, semua_harga, semua_jumlah, subtotal, total_diskon, persen_diskon):
    print("============================================")
    print("           STRUK PEMBELIAN ANDA")
    print("============================================")
    print("Detail Belanja:")

    for i in range(len(semua_nama)):
        nama = semua_nama[i]
        harga = semua_harga[i]
        jumlah = semua_jumlah[i]
        total_item = harga * jumlah
        print(f"{i+1}. {nama} ({jumlah} x Rp {harga}) = Rp {total_item}")

    print("--------------------------------------------")
    print(f"Subtotal         : Rp {subtotal}")
    print(f"Diskon ({persen_diskon}%)    : - Rp {total_diskon}")
    print("--------------------------------------------")
    print(f"Total Bayar      : Rp {subtotal - total_diskon}")
    print("============================================")
    print("     TERIMA KASIH TELAH BERBELANJA!")
    print("============================================")

