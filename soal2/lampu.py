class Lampu:
  # Atribut kelas untuk menghitung jumlah total objek Lampu
  jumlah_lampu = 0

  def __init__(self, nama):
    self.nama = nama
    self.aktif = False
    self.kecerahan = 0
    # Setiap kali objek dibuat, jumlah_lampu bertambah 1
    Lampu.jumlah_lampu += 1

  def nyalakan(self):
    self.aktif = True
    self.kecerahan = 100

  def matikan(self):
    self.aktif = False
    self.kecerahan = 0

  def atur(self, nilai):
    if nilai < 0:
      self.kecerahan = 0
    elif nilai > 100:
      self.kecerahan = 100
    else:
      self.kecerahan = nilai

  def __str__(self):
    return (
        f"Lampu {self.nama}: aktif = {self.aktif}, kecerahan = {self.kecerahan}"
    )