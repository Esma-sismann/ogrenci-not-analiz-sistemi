from functools import reduce

def harf_notu_hesapla(ortalama):
    if ortalama >= 90: return "AA"
    elif ortalama >= 80: return "BA"
    elif ortalama >= 70: return "BB"
    elif ortalama >= 60: return "CB"
    elif ortalama >= 50: return "CC"
    else: return "FF"

ogrenciler = []
hatalar = []

# 1. Dosyayı Okuma ve Hata Yakalama
try:
    with open("ogrenciler.txt", "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()
        
        for satir in satirlar:
            satir = satir.strip()
            if not satir: continue
            
            parcalar = satir.split(",")
            isim = parcalar[0]
            
            try:
                # 2. ve 3. Adım: Map ile notları sayıya çevirme ve Hataları yakalama
                notlar = list(map(int, parcalar[1:]))
                
                # Ekstra Görev: Not aralığı kontrolü (0-100)
                if not all(0 <= n <= 100 for n in notlar):
                    raise ValueError("Notlar 0-100 arasinda olmali.")

                # 4. Ortalama Hesaplama (Reduce kullanımı)
                ortalama = reduce(lambda x, y: x + y, notlar) / len(notlar)
                
                # Veriyi listeye ekle
                ogrenciler.append({
                    "isim": isim,
                    "notlar": notlar,
                    "ortalama": ortalama,
                    "harf": harf_notu_hesapla(ortalama)
                })
                
            except Exception as e:
                hatalar.append(f"Hatali satir: {satir} | Hata sebebi: {e}")

except FileNotFoundError:
    print("Hata: ogrenciler.txt dosyasi bulunamadi!")
    exit()

# 6. Filter ile Geçenleri ve Kalanları Ayırma
gecenler = list(filter(lambda o: o["ortalama"] >= 50, ogrenciler))
kalanlar = list(filter(lambda o: o["ortalama"] < 50, ogrenciler))

# 7. Zip ile İsim ve Harf Notlarını Eşleştirme
isimler = list(map(lambda x: x["isim"], ogrenciler))
harfler = list(map(lambda x: x["harf"], ogrenciler))
isim_harf_zip = list(zip(isimler, harfler))

# 8. Enumerate ile Sıralı Rapor Yazma (sonuclar.txt)
with open("sonuclar.txt", "w", encoding="utf-8") as f:
    for i, ogrenci in enumerate(ogrenciler, 1):
        f.write(f"{i}. {ogrenci['isim']} - Ortalama: {ogrenci['ortalama']:.2f} - Harf: {ogrenci['harf']}\n")

# 9. All ve Any Kullanımı
tum_ogrenciler_gecti_mi = all(o["ortalama"] >= 50 for o in ogrenciler)
sinifta_kalan_var_mi = any(o["ortalama"] < 50 for o in ogrenciler)

# Hataları, Geçenleri ve Kalanları Dosyalara Yazma
with open("hatalar.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(hatalar))

with open("gecenler.txt", "w", encoding="utf-8") as f:
    for g in gecenler: f.write(f"{g['isim']}: {g['ortalama']:.2f}\n")

with open("kalanlar.txt", "w", encoding="utf-8") as f:
    for k in kalanlar: f.write(f"{k['isim']}: {k['ortalama']:.2f}\n")

# Ekstra Görevler: Sınıf Analizi
if ogrenciler:
    sinif_ortalamasi = sum(o["ortalama"] for o in ogrenciler) / len(ogrenciler)
    en_yuksek = max(ogrenciler, key=lambda x: x["ortalama"])
    en_dusuk = min(ogrenciler, key=lambda x: x["ortalama"])

    print("--- Analiz Tamamlandi ---")
    print(f"Sinif Ortalamasi: {sinif_ortalamasi:.2f}")
    print(f"En Başarili: {en_yuksek['isim']} ({en_yuksek['ortalama']})")
    print(f"Herkes geçti mi?: {'Evet' if tum_ogrenciler_gecti_mi else 'Hayir'}")