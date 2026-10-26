import os


def baca_log(nama_file):
  data_valid = []
  data_ditolak = []

  with open(nama_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

  for idx, line in enumerate(lines, start=1):
    baris_teks = line.strip()
    # Lewati baris header (baris 1)
    if idx == 1:
      continue

    if not baris_teks:
      data_ditolak.append({
          "no_baris": idx,
          "isi": baris_teks,
          "alasan": "Baris kosong",
      })
      continue

    # Pisahkan kolom berdasarkan koma
    parts = [p.strip() for p in baris_teks.split(",")]
    if len(parts) != 2:
      data_ditolak.append({
          "no_baris": idx,
          "isi": baris_teks,
          "alasan": (
              f"Jumlah kolom tidak dua (ditemukan {len(parts)} kolom)"
          ),
      })
      continue

    waktu, nilai_str = parts[0], parts[1]

    # Cek apakah nilai berupa angka
    try:
      nilai = float(nilai_str)
    except ValueError:
      data_ditolak.append({
          "no_baris": idx,
          "isi": baris_teks,
          "alasan": f"Nilai debit bukan angka ('{nilai_str}')",
      })
      continue

    # Cek batas rentang sensor (5 sampai 25 inklusif)
    if not (5 <= nilai <= 25):
      data_ditolak.append({
          "no_baris": idx,
          "isi": baris_teks,
          "alasan": f"Nilai debit {nilai} di luar batas sensor (5 - 25)",
      })
      continue

    data_valid.append({"no_baris": idx, "waktu": waktu, "nilai": nilai})

  return data_valid, data_ditolak


def galat_absolut(hasil, acuan):
  return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
  if acuan == 0:
    raise ValueError("Nilai acuan tidak boleh nol.")
  return (abs(hasil - acuan) / acuan) * 100


if __name__ == "__main__":
  # Sesuaikan path file jika dijalankan dari root folder
  file_path = "log_debit.csv"
  if not os.path.exists(file_path) and os.path.exists(
      os.path.join("soal5", "log_debit.csv")
  ):
    file_path = os.path.join("soal5", "log_debit.csv")

  valid, ditolak = baca_log(file_path)

  print("=== HASIL VALIDASI SOAL 5b ===")
  print(f"Jumlah data valid   : {len(valid)}")
  print(f"Jumlah data ditolak : {len(ditolak)}")

  print("\nAlasan penolakan data:")
  for d in ditolak:
    print(
        f"- Baris {d['no_baris']} ('{d['isi']}'): {d['alasan']}"
    )

  if valid:
    nilai_list = [v["nilai"] for v in valid]
    rata_valid = sum(nilai_list) / len(nilai_list)
    print(f"Rata-rata data valid: {rata_valid:.2f}")

    print("\n=== HASIL PERHITUNGAN SOAL 5c ===")
    acuan = 13.5714
    g_abs = galat_absolut(rata_valid, acuan)
    g_rel = galat_relatif(rata_valid, acuan)
    status = "LULUS" if g_rel <= 0.5 else "TIDAK LULUS"

    print(f"Galat absolut       : {g_abs:.4f}")
    print(f"Galat relatif (%)   : {g_rel:.4f}%")
    print(f"Status              : {status}")