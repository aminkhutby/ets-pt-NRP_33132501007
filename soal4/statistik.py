def rentang(data):
    return (min(data), max(data))

def ringkasan(data):
    return {
        "jumlah": len(data),
        "min": min(data),
        "maks": max(data),
        "rata": sum(data) / len(data)
    }

# Pengujian sesuai soal
if __name__ == "__main__":
    data_uji = [12.0, 15.0, 15.0]
    
    r = rentang(data_uji)
    ringk = ringkasan(data_uji)
    
    print(r)
    print(ringk)
    print(ringk["rata"])