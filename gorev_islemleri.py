def gorev_ekle(karakter):
    baslik = input("Görev başlığı: ")
    print("Zorluklar: kolay, orta, zor")
    zorluk = input("Zorluk seçin: ").lower()

    # Görsel 3'teki koşullu durumlar
    if zorluk == "kolay":
        xp = 10
    elif zorluk == "orta":
        xp = 30
    elif zorluk == "zor":
        xp = 50
    else:
        print("Geçersiz zorluk! Kolay olarak atandı.")
        zorluk, xp = "kolay", 10

    yeni_gorev = {
        "baslik": baslik,
        "zorluk": zorluk,
        "xp": xp,
        "tamamlandi": False
    }
    karakter.gorevler.append(yeni_gorev)
    print(f"'{baslik}' eklendi.")

def gorevleri_listele(karakter):
    if not karakter.gorevler:
        print("\nListe boş.")
        return
    # Görsel 8'deki formatta listeleme
    for i, g in enumerate(karakter.gorevler, 1):
        durum = "Tamamlandı" if g['tamamlandi'] else "Bekliyor"
        print(f"{i}- {g['baslik']} | Zorluk: {g['zorluk']} | XP: {g['xp']} | Durum: {durum}")

def gorev_tamamla(karakter):
    gorevleri_listele(karakter)
    if not karakter.gorevler: return
    try:
        no = int(input("\nTamamlanan görev no: ")) - 1
        g = karakter.gorevler[no]
        if g['tamamlandi']:
            print("\nBu görev zaten tamamlanmış.")
        else:
            g['tamamlandi'] = True
            karakter.xp_ekle(g['xp'])
            print(f"\nGörev tamamlandı! {g['xp']} XP kazandın.")
    except:
        print("\nHatalı giriş!")

def zorluga_gore_listele(karakter):
    z = input("Hangi zorluk? (kolay/orta/zor): ").lower()
    for g in karakter.gorevler:
        if g['zorluk'] == z:
            durum = "Tamamlandı" if g['tamamlandi'] else "Bekliyor"
            print(f"- {g['baslik']} | Durum: {durum}")