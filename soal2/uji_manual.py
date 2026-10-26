from debit import hitung_rata_rata, cari_terendah, cek_status

print("Rata-rata:", hitung_rata_rata([10, 20, 30]))
print("Terendah:", cari_terendah([12.5, 14.0, 11.0]))

for v in [9.9, 10, 20, 20.1]:
    val = float(input(f"Masukkan nilai debit ({v}): ") or v)
    print(f"Nilai {val} -> Status: {cek_status(val)}")