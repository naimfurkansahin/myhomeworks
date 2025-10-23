'''
yazan : nAİm
16.10.2025
    bu üçüncü ödevim telefon rehberi yapıyorum.

'''

if __name__ == "__main__":
    # Ödev 4: Telefon Rehberi (dict)
    telefon_rehberi = {}

    while True:
        secim = input("Seçiminiz. (ekle/ara/sil/listele/güncelle/çık)")
        if secim == "çık":
            break

        elif secim == "ekle":
            isim = input("Eklemek istediğiniz kişinin ismi: ")
            numara = input("Eklemek istediğiniz kişinin numarası: ")
            if isim in telefon_rehberi:
             print("Bu kişi zaten kayıtlı!")
            elif numara in telefon_rehberi.values():
             print("Bu numara zaten kayıtlı!")
            else:
             telefon_rehberi[isim] = numara
             print(f"{isim} rehbere eklendi.")

        elif secim == "ara":
            ara = input("İsim veya ismin bir kısmını giriniz: ").lower()
            bulunanlar = {isim: num for isim, num in telefon_rehberi.items() if ara in isim.lower()}
            if bulunanlar:
                for isim, num in bulunanlar.items():
                    print(f"{isim}: {num}")
            else:
                print("Eşleşen kişi bulunamadı.")

        elif secim == "sil":
            sil = input("Silmek istediğiniz kişinin ismi: ")
            if sil in telefon_rehberi:
               del telefon_rehberi[sil]
               print(f"{sil} rehberden silindi.")
            else:
               print("Rehberde", sil, "adında birisi yok.")

        elif secim == "güncelle":
            isim = input("Numarasını güncellemek istediğiniz kişinin ismi: ")
            if isim in telefon_rehberi:
                yeni_numara = input("Yeni numarayı giriniz: ")
                telefon_rehberi[isim] = yeni_numara
                print(f"{isim} adlı kişinin numarası güncellendi.")
            else:
                print("Rehberde böyle bir kişi yok.")


        elif secim == "listele":
            if not telefon_rehberi:
               print("Rehber boş.")
            else:
                print("\n--- TELEFON REHBERİ ---")
                for isim, numara in telefon_rehberi.items():
                  print(f"{isim}: {numara}")
                print("-----------------------\n")
        else:
            print("Lütfen geçerli bir işlem seçiniz.")

