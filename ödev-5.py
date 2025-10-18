#nAİm
#18.10.2025
#basit bankamatik



if  __name__ == "__main__":

    bakiye = 0

    while True:
        print("\n---- BANKA ----")
        print("1- Bakiye görüntüle ")
        print("2- Para yatır ")
        print("3- Para çek ")
        print("4- Çıkış ")
        print("---------------\n")

        secim = input("Seçiminizi yapın (1-4): ")


        if secim == "1":
            print(f"Bakiyeniz: {bakiye} TL")

        elif secim == "2":
            try:
                miktar = float(input("Yatırmak istediğiniz tutarı giriniz: "))
                if miktar < 0:
                    print("Lütfen geçerli bir sayı giriniz!")
                else:
                    bakiye += miktar
                    print(f"{miktar} TL yatırıldı. Bakiyeniz: {bakiye} TL")

            except ValueError:
                print("Lütfen sayısal değer giriniz.")

        elif secim == "3":
            try:
                miktar = float(input("Çekmek istediğiniz tutarı giriniz: "))
                if miktar < 0:
                    print("Lütfen geçerli bir sayı giriniz!")
                elif miktar > bakiye:
                    print("Bakiye yetersiz!")
                else:
                    bakiye -= miktar
                    print(f"{miktar} TL çekildi. Bakiyeniz: {bakiye} TL")

            except ValueError:
                print("Lütfen geçerli bir değer giriniz.")
                
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Hata! Lütfen 1-4 arasında bir değer giriniz.")