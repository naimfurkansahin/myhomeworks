#nAİm
#25.10.2025
#basit şifre oyunu

import random
from collections import Counter

def yeni_sayi_uret():
    # 0000 - 9999 arası, başında 0 olabilir (her zaman 4 haneli string)
    return f"{random.randint(0, 9999):04d}"

def geri_bildirim(sifre, tahmin):
    dogru_pozisyon = sum(1 for s, t in zip(sifre, tahmin) if s == t)
    ortak = sum((Counter(sifre) & Counter(tahmin)).values())
    dogru_rakam_yanlis_yer = ortak - dogru_pozisyon
    return dogru_pozisyon, dogru_rakam_yanlis_yer

def oyun():
    print("=== 4 HANELİ SAYI TAHMİN OYUNU ===")
    print("Bilgisayar 4 haneli rastgele bir sayı tuttu. (0000 - 9999)")
    print("Tahmin et. Her seferinde 'doğru yer' ve 'doğru rakam yanlış yer' bilgisi alacaksın.")
    print("Çıkmak için 'q' yaz.\n")

    sifre = yeni_sayi_uret()

    deneme_sayisi = 0
    while True:
        try:
            tahmin = input("4 haneli tahminin: ").strip()
            if tahmin.lower() == 'q':
                print("Oyundan çıkılıyor. Doğru sayı:", sifre)
                break

            if not (tahmin.isdigit() and len(tahmin) == 4):
                print("Hata: Lütfen 4 haneli bir sayı gir (ör. 0427).")
                continue

            deneme_sayisi += 1
            dogru_poz, dogru_rpyy = geri_bildirim(sifre, tahmin)

            if dogru_poz == 4:
                print(f"Tebrikler! {deneme_sayisi}. denemede bildin. Sayı: {sifre}")
                break
            else:
                print(f"Doğru yer: {dogru_poz} | Doğru rakam (yanlış yerde): {dogru_rpyy}")
        except KeyboardInterrupt:
            print("\nOyundan çıkıldı (KeyboardInterrupt). Doğru sayı:", sifre)
            break
        except Exception as e:
            print("Beklenmeyen hata:", e)
            break

if __name__ == "__main__":
    while True:
        oyun()
        tekrar = input("Tekrar oyna? (e/h): ").strip().lower()
        if tekrar != 'e':
            print("Görüşürüz!")
            break
