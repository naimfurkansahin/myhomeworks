
# nAİm
# 16.10.2025
# telefon rehberi
    
import json
import os

# Masaüstü yolunu otomatik bulalım
masaustu = os.path.join(os.path.expanduser("~"), "Desktop")
dosya_yolu = os.path.join(masaustu, "rehber.json")

def kaydet():
    """Rehberi masaüstündeki JSON dosyasına kaydeder."""
    with open(dosya_yolu, "w", encoding="utf-8") as f:
        json.dump(telefon_rehberi, f, ensure_ascii=False, indent=4)

def yukle():
    """Program başlarken masaüstündeki dosyadan rehberi yükler."""
    global telefon_rehberi
    try:
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            telefon_rehberi = json.load(f)
    except FileNotFoundError:
        telefon_rehberi = {}

if __name__ == "__main__":
    yukle()

    while True:
        print("""
--- TELEFON REHBERİ ---
1. Kişi Ekle
2. Kişi Ara
3. Kişi Sil
4. Listele
5. Güncelle
6. Çık
------------------------
""")

        secim = input("Seçiminiz (1-6): ")

        if secim == "6" or secim.lower() == "çık":
            kaydet()
            print("Değişiklikler kaydedildi. Programdan çıkılıyor...")
            break

        elif secim == "1" or secim.lower() == "ekle":
            isim = input("Eklemek istediğiniz kişinin ismi: ").strip()
            numara = input("Eklemek istediğiniz kişinin numarası: ").strip()

            if not numara.isdigit() or len(numara) < 10:
                print("Lütfen geçerli bir numara giriniz (en az 10 haneli).")
                continue

            if isim in telefon_rehberi:
                print("Bu kişi zaten kayıtlı!")
            elif numara in telefon_rehberi.values():
                print("Bu numara zaten kayıtlı!")
            else:
                telefon_rehberi[isim] = numara
                print(f"{isim} rehbere eklendi.")
                kaydet()

        elif secim == "2" or secim.lower() == "ara":
            ara = input("İsim veya ismin bir kısmını giriniz: ").lower()
            bulunanlar = {isim: num for isim, num in telefon_rehberi.items() if ara in isim.lower()}

            if bulunanlar:
                print("\n--- Arama Sonuçları ---")
                for isim, num in bulunanlar.items():
                    print(f"{isim}: {num}")
                print("-----------------------\n")
            else:
                print("Eşleşen kişi bulunamadı.")

        elif secim == "3" or secim.lower() == "sil":
            sil = input("Silmek istediğiniz kişinin ismi: ").strip()
            if sil in telefon_rehberi:
                del telefon_rehberi[sil]
                print(f"{sil} rehberden silindi.")
                kaydet()
            else:
                print(f"Rehberde '{sil}' adında birisi yok.")

        elif secim == "4" or secim.lower() == "listele":
            if not telefon_rehberi:
                print("Rehber boş.")
            else:
                print("\n--- TELEFON REHBERİ ---")
                for isim, numara in sorted(telefon_rehberi.items()):
                    print(f"{isim}: {numara}")
                print(f"Toplam {len(telefon_rehberi)} kişi kayıtlı.")
                print("-----------------------\n")

        elif secim == "5" or secim.lower() == "güncelle":
            isim = input("Numarasını güncellemek istediğiniz kişinin ismi: ").strip()
            if isim in telefon_rehberi:
                yeni_numara = input("Yeni numarayı giriniz: ").strip()
                if not yeni_numara.isdigit() or len(yeni_numara) < 10:
                    print("Geçersiz numara!")
                    continue
                telefon_rehberi[isim] = yeni_numara
                print(f"{isim} adlı kişinin numarası güncellendi.")
                kaydet()
            else:
                print("Rehberde böyle bir kişi yok.")

        else:
            print("Lütfen geçerli bir işlem seçiniz (1-6).")
