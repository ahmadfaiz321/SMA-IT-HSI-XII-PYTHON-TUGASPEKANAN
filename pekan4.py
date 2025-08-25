
#Aplikasi Polling Sederhana

SURVEI = [
    {
        "pertanyaan": "siapa sahabat favorite mu?",
        "opsi": ["abu bakar", "umar bin khotab", "utsman", "ali" ]
    },
    {
        "pertanyaan": "siapa yang meriwayati hadits?",
        "opsi": ["abu hurairah", "umar bin khatab", "jabir"]
    },
    {
        "pertanyaan": "perang apa saja yang km tauk?",
        "opsi": ["badar", "khibar", "uhud", "khandak"]
    }
]

# Inisialisasi hasil polling dengan semua opsi bernilai 0
hasil_polling = {}
for item_survei in SURVEI:
    for opsi in item_survei["opsi"]:
        hasil_polling[opsi] = 0

print("="*44)
print(" SELAMAT DATANG DI APLIKASI POLLING")
print("="*44)

# Loop utama untuk setiap pertanyaan
for idx, item_survei in enumerate(SURVEI, start=1):
    print(f"\nPertanyaan {idx}: {item_survei['pertanyaan']}")
    for opsi in item_survei["opsi"]:
        print(f" - {opsi}")
    
    # Validasi input
    while True:
        jawaban = input("Jawaban Anda: ").strip()
        if jawaban in item_survei["opsi"]:
            hasil_polling[jawaban] += 1
            print(f"> {jawaban}")
            print("--- Terima kasih! ---")
            break
        else:
            print("Jawaban tidak valid. Silakan pilih dari opsi yang tersedia.")

# Menampilkan hasil polling
print("="*44)
print(" HASIL POLLING")
print("="*44)

total_suara = sum(hasil_polling.values())

for opsi, jumlah in hasil_polling.items():
    persentase = (jumlah / total_suara * 100) if total_suara > 0 else 0
    print(f"{opsi} : {jumlah} suara ({persentase:.2f}%)")

print("="*44)