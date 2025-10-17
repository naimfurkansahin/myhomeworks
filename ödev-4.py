'''
yazan : nAİm
16.10.2025
    bu dördüncü ödevim not defteri yapıyorum.

'''

import os

if __name__ == "__main__":
    # Ödev 5: Basit Not Defteri (Dosya İşlemleri)

    # DONE[1]: "notlar.txt" adında bir dosya oluşturun (yoksa oluşturulsun)
    try:
        open("notlar.txt", "x").close()
    except FileExistsError:
        pass

    while True:
        # DONE[2]: Kullanıcıya menü gösterin
        print("\n--- NOT DEFTERİ ---")
        print("1. Not ekle")
        print("2. Notları listele")
        print("3. Not sil")
        print("4. Tüm notları temizle")
        print("5. Çık")
        print("-------------------\n")

        secim = input("Seçiminizi yapın (1-5): ")

        # DONE[3]: "ekle" seçilince kullanıcıdan metin alın ve dosyaya ekleyin
        if secim == "1":
            not_metni = input("Notunuzu yazın: ")
            with open("notlar.txt", "a", encoding="utf-8") as dosya:
                dosya.write(not_metni + "\n")
            print("✅ Not eklendi.")

        # DONE[4]: "listele" seçilince dosyadaki tüm notları ekrana yazdırın
        elif secim == "2":
            with open("notlar.txt", "r", encoding="utf-8") as dosya:
                notlar = dosya.readlines()
            if not notlar:
                print("📂 Henüz hiç not yok.")
            else:
                print("\n--- KAYITLI NOTLAR ---")
                for i, n in enumerate(notlar, start=1):
                    print(f"{i}. {n.strip()}")
                print("------------------------")

        # DONE[5]: "sil" seçilince kullanıcıdan bir satır numarası alın, o notu silin
        elif secim == "3":
            with open("notlar.txt", "r", encoding="utf-8") as dosya:
                notlar = dosya.readlines()

            if not notlar:
                print("Silinecek not yok.")
                continue

            print("\n--- KAYITLI NOTLAR ---")
            for i, n in enumerate(notlar, start=1):
                print(f"{i}. {n.strip()}")
            print("------------------------")

            try:
                sil_no = int(input("Silmek istediğiniz notun numarasını girin: "))
                if 1 <= sil_no <= len(notlar):
                    silinen = notlar.pop(sil_no - 1)
                    with open("notlar.txt", "w", encoding="utf-8") as dosya:
                        dosya.writelines(notlar)
                    print(f"🗑️ '{silinen.strip()}' notu silindi.")
                else:
                    print("Geçersiz numara!")
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")

        # DONE[6]: "temizle" seçilince tüm notları silin (dosyayı boşaltın)
        elif secim == "4":
            onay = input("Tüm notlar silinecek! Emin misiniz? (e/h): ")
            if onay.lower() == "e":
                open("notlar.txt", "w").close()
                print("📁 Tüm notlar temizlendi.")
            else:
                print("İşlem iptal edildi.")

        elif secim == "5":
            print("👋 Not defteri kapatılıyor...")
            break

        else:
            print("⚠️ Geçersiz seçim! Lütfen 1-5 arasında bir değer girin.")
