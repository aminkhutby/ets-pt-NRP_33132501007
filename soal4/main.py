from soal4.perangkat import SensorSuhu, SensorDebit

# 1. Membuat objek sensor
suhu = SensorSuhu("Suhu")
debit = SensorDebit("Debit", "L/menit")

# 2. Mengisi data
suhu.baca(30.1)
suhu.baca(30.6)
suhu.baca(30.3)

debit.baca(12.0)
debit.baca(15.0)
debit.baca(15.0)

# 3. Memasukkan keduanya ke satu list dan melakukan perulangan polimorfisme
daftar_perangkat = [suhu, debit]

for p in daftar_perangkat:
    print(f"{p.nama} -> {p.proses()}")