import requests
from datetime import datetime

def son_depremleri_getir():
    usgs_api_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    response = requests.get(usgs_api_url)
    if response.status_code == 200:
        data = response.json()
        print("Son Depremler:")
        for deprem in data['features']:
            yer = deprem['properties']['place']
            buyukluk = deprem['properties']['mag']
            tarih_unix = deprem['properties']['time'] / 1000  # Unix zaman damgası
            tarih = datetime.utcfromtimestamp(tarih_unix).strftime('%Y-%m-%d %H:%M:%S UTC')

            print(f"{tarih} - {yer} - Büyüklük: {buyukluk}")
    else:
        print(f"Hata: {response.status_code} - Veri alınamadı.")

if __name__ == "__main__":
    son_depremleri_getir()
