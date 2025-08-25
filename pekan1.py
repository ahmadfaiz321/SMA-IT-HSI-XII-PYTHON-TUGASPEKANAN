

print("============================================")
print("AHLAN WA SAHLAN DI PROGRAM KASIR CERDAS!")
print("============================================")


print("\n--- Masukkan Detail Barang 1 ---")
nama_barang_1 = input("Nama Barang: ")
harga_1 = float(input("Harga Satuan (Rp): "))
jumlah_1 = int(input("Jumlah: "))


print("\n--- Masukkan Detail Barang 2 ---")
nama_barang_2 = input("Nama Barang: ")
harga_2 = float(input("Harga Satuan (Rp): "))
jumlah_2 = int(input("Jumlah: "))

print("\nMenghitung total...")


total_1 = harga_1 * jumlah_1
total_2 = harga_2 * jumlah_2
subtotal = total_1 + total_2


diskon = 10.
persen_diskon = 0

if subtotal > 200000:
    persen_diskon = 10
    diskon = subtotal * 0.10
elif subtotal > 100000:
    persen_diskon = 5
    diskon = subtotal * 0.05

total_setelah_diskon = subtotal - diskon


ppn = total_setelah_diskon * 0.11
total_final = total_setelah_diskon + ppn


uang_dibayar = float(input("\nMasukkan jumlah uang yang dibayarkan pelanggan (Rp): "))
kembalian = uang_dibayar - total_final

print("============================================")
print("           STRUK PEMBELIAN ANDA             ")
print("============================================")
print("Detail Belanja:")
print(f"1. {nama_barang_1} ({jumlah_1} x Rp {harga_1}) = Rp {total_1}")
print(f"2. {nama_barang_2} ({jumlah_2} x Rp {harga_2}) = Rp {total_2}")
print("--------------------------------------------")
print(f"Subtotal           : Rp {subtotal}")
print(f"Diskon ({persen_diskon}%)     : - Rp {diskon}")
print(f"Total Setelah Diskon : Rp {total_setelah_diskon}")
print(f"PPN (11%)           : + Rp {ppn}")
print("--------------------------------------------")
print(f"Total Akhir         : Rp {total_final}")
print(f"Uang Dibayar        : Rp {uang_dibayar}")
print(f"Kembalian           : Rp {kembalian}")
print("============================================")
print("     TERIMA KASIH TELAH BERBELANJA          ")
print("============================================")
