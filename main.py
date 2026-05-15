from karakter import Karakter
import gorev_islemleri

def karakter_olustur():
    ad = input("Karakter adı: ")
    print("1- Yazilimci\n2- Tasarimci\n3- Veri Analisti")
    secim = input("Sinif seç (1-3): ")
    siniflar = {"1": "Yazilimci", "2": "Tasarimci", "3": "Veri Analisti"}
    return Karakter(ad, siniflar.get(secim, "Gezgin"))

def main():
    oyuncu = None
    while True:
        print("\n=== GÖREV LONCASI ===")
        print("1- Karakter Oluştur\n2- Görev Ekle\n3- Görevleri Listele\n4- Görev Tamamla")
        print("5- Karakter Durumu\n6- Zorluğa Göre Görevler\n7- Çikiş")
        
        s = input("Seçim: ")
        if s == "1": oyuncu = karakter_olustur()
        elif s == "7": break
        elif oyuncu is None: print("Önce karakter oluştur!")
        elif s == "2": gorev_islemleri.gorev_ekle(oyuncu)
        elif s == "3": gorev_islemleri.gorevleri_listele(oyuncu)
        elif s == "4": gorev_islemleri.gorev_tamamla(oyuncu)
        elif s == "5": oyuncu.durum_goster()
        elif s == "6": gorev_islemleri.zorluga_gore_listele(oyuncu)

if __name__ == "__main__":
    main()