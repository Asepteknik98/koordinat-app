import requests
import urllib.parse

def cari_lokasi(nama_tempat):
    # Encode nama tempat agar aman dalam URL
    query = urllib.parse.quote(nama_tempat)
    url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json&addressdetails=1&limit=1"
    
    headers = {
        'User-Agent': 'LokasiApp/1.0 (your_email@example.com)'  # WAJIB isi agar tidak diblok
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                hasil = data[0]
                alamat_lengkap = hasil.get("display_name", "Alamat tidak tersedia")
                lat = hasil.get("lat", "-")
                lon = hasil.get("lon", "-")
                return {
                    "alamat": alamat_lengkap,
                    "latitude": lat,
                    "longitude": lon
                }
            else:
                return {"error": "Lokasi tidak ditemukan. Coba gunakan nama yang lebih umum atau singkat."}
        else:
            return {"error": f"HTTP Error: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

# Masukkan nama tempat yang ingin dicari
nama_tempat = "Cikupa, Tangerang, Banten, Indonesia"
hasil = cari_lokasi(nama_tempat)

# Cetak hasil
print("="*40)
if "error" in hasil:
    print("Error:", hasil["error"])
else:
    print("Alamat ditemukan:")
    print("Alamat Lengkap :", hasil["alamat"])
    print("Latitude       :", hasil["latitude"])
    print("Longitude      :", hasil["longitude"])
print("="*40)