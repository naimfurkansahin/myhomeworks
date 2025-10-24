
# nAİm
# 16.10.2025
# arayüzlü bir üye kayıt uygulaması


if __name__ == "__main__":
    baslik = "Üye Kayıt Sistemi"

    uye_adlari = []
    uye_soyadlari = []
    uye_numaralari = []

    while True:
        print("-" * 100)
        print(f"| {baslik:^94} |x|")
        print("-" * 100)
        print(f"| 1 - Üye ekle {' ' * 84}|")
        print(f"| 2 - Üye sil {' ' * 85}|")
        print(f"| 3 - Üye ara {' ' * 85}|")
        print(f"| 4 - Üye listele {' ' * 81}|")
        print(f"| 5 - Çıkış {' ' * 87}|")
        print(f"|{' ' * 98}|")

        try:
            secim = int(input("| Hangi işlemi yapmak istersiniz?: "))
            if secim < 1 or secim > 5:
                print("| Hata! Lütfen geçerli bir değer giriniz.")
                continue
        except ValueError:
            print("| Hata! Lütfen geçerli bir sayı giriniz.")
            continue

        # ---------------- ÜYE EKLEME ----------------
        if secim == 1:
            while True:
                try:
                    uye_sayisi = int(input("| Kaç üye kaydedeceksiniz?: "))
                    break
                except ValueError:
                    print("| Hata! Lütfen geçerli bir sayı giriniz.")

            for sıra in range(uye_sayisi):
                uye_adlari.append(input(f"| {sıra + 1}. Üye adını giriniz: "))
                uye_soyadlari.append(input(f"| {sıra + 1}. Üye soyadını giriniz: "))
                while True:
                    try:
                        uye_numaralari.append(int(input(f"| {sıra + 1}. Üye numarasını giriniz: ")))
                        break
                    except ValueError:
                        print("| Hata! Lütfen geçerli bir sayı giriniz.")

            if uye_sayisi > 1:
                print("| Üyeler kaydedildi.")
            else:
                print("| Üye kaydedildi.")

        # ---------------- ÜYE SİLME ----------------
        elif secim == 2:
            if len(uye_numaralari) == 0:
                print("| Henüz kayıtlı üye yok.")
                continue

            try:
                uye_sil = int(input("| Silmek istediğiniz üye numarasını girin: "))

                if uye_sil in uye_numaralari:
                    sil_index = uye_numaralari.index(uye_sil)
                    del uye_adlari[sil_index]
                    del uye_soyadlari[sil_index]
                    del uye_numaralari[sil_index]
                    print(f"| {uye_sil} numaralı üye silindi.")
                else:
                    print("| Üye bulunamadı.")
            except ValueError:
                print("| Hata! Lütfen geçerli bir sayı giriniz.")

        # ---------------- ÜYE ARAMA ----------------
        elif secim == 3:
            if len(uye_adlari) == 0:
                print("| Henüz kayıtlı üye yok.")
            else:
                arama = input("| Aramak istediğiniz üyenin adını, soyadını veya numarasını girin: ").strip()

                bulundu = False
                print("-" * 100)
                print(f"| {'No':^8} | {'İsim':<30} | {'Soyisim':<30} | {'Numara':<20}|")
                print("-" * 100)

                for i in range(len(uye_adlari)):
                    # Ad, soyad veya numara eşleşirse göster
                    if (arama.lower() in uye_adlari[i].lower()) or \
                       (arama.lower() in uye_soyadlari[i].lower()) or \
                       (arama == str(uye_numaralari[i])):
                        print(f"| {i+1:^8} | {uye_adlari[i]:<30} | {uye_soyadlari[i]:<30} | {uye_numaralari[i]:<20}|")
                        bulundu = True

                if not bulundu:
                    print("| Aradığınız bilgilere uygun üye bulunamadı.")

                print("-" * 100)

        # ---------------- ÜYE LİSTELEME ----------------
        elif secim == 4:
            if len(uye_adlari) == 0:
                print("| Henüz kayıtlı üye yok.")
                continue

            print("-" * 100)
            print(f"| {'No':^8} | {'İsim':<30} | {'Soyisim':<30} | {'Numara':<20}|")
            print("-" * 100)
            for sıra in range(len(uye_adlari)):
                print(f"| {sıra + 1:^8} | {uye_adlari[sıra]:<30} | {uye_soyadlari[sıra]:<30} | {uye_numaralari[sıra]:<20}|")
            print("-" * 100)

        # ---------------- ÇIKIŞ ----------------
        elif secim == 5:
            print("| Çıkış yapılıyor...")
            break