class Karakter:
    def __init__(self, ad, sinif):
        self.ad = ad
        self.sinif = sinif
        self.seviye = 1
        self.xp = 0
        self.gorevler = []

    def xp_ekle(self, miktar):
        self.xp += miktar
        # Görsel 9'daki seviye hesaplama mantığı
        yeni_seviye = (self.xp // 100) + 1
        if yeni_seviye > self.seviye:
            self.seviye = yeni_seviye
            print(f"\n[!] TEBRİKLER! {self.seviye}. Seviyeye ulaştın!")

    def durum_goster(self):
        tamamlanan = sum(1 for g in self.gorevler if g['tamamlandi'])
        print("\n" + "="*20)
        print(f"Ad: {self.ad}")
        print(f"Sınıf: {self.sinif}")
        print(f"Seviye: {self.seviye}")
        print(f"XP: {self.xp}")
        print(f"Toplam Görev: {len(self.gorevler)}")
        print(f"Tamamlanan Görev: {tamamlanan}")
        print("="*20)