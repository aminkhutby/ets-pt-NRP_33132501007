def hitung_rata_rata(data):
    # Pastikan rumus rata-rata benar (misal: sum(data) / len(data))
    return sum(data) / len(data)

def cari_terendah(data):
    # Pastikan mencari nilai minimum
    return min(data)

def cek_status(nilai):
    # Logika status debit air
    if nilai < 10:
        return "Rendah"
    elif nilai <= 20:
        return "Normal"
    else:
        return "Tinggi"
    
def hitung_rata_rata(data):
    """
    Menghitung nilai rata-rata dari list data debit air.
    Input: data (list berisi angka float/int)
    Output: float (nilai rata-rata)
    """
    return sum(data) / len(data)


def cari_terendah(data):
    """
    Mencari nilai terkecil dari list data debit air.
    Input: data (list berisi angka float/int)
    Output: float/int (nilai paling rendah)
    """
    return min(data)


def cek_status(nilai):
    """
    Menentukan status debit air berdasarkan nilai pembacaan.
    Input: nilai (float/int)
    Output: str (status debit)
    Batas kategori: 
      - 'Rendah' jika nilai < 10
      - 'Normal' jika nilai antara 10 sampai 20
      - 'Tinggi' jika nilai > 20
    """
    if nilai < 10:
        return "Rendah"
    elif nilai <= 20:
        return "Normal"
    else:
        return "Tinggi"