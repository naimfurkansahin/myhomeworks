'''
yazan : nAİm
16.10.2025
    bu ikinci ödevim kulanıcıdan yaş alıp onu kategorilendirmek.

'''

if __name__ == "__main__":
    # Ödev 2: Yaş Kontrolü

    # DONE[1]: input() ile kullanıcıdan yaş al
    yas = input("Yaşınızı giriniz: ")

    # DONE[2]: rakam olmayan değerler için uyarı verin
    try: 
        yas_int = int(yas)
    except:
        print("Hatalı sayı girdiniz.")
        exit()

    # DONE[3]: mantıksal aralık kontrolü: yaş <0 veya >100 ise uyarı
    if yas_int < 0 or yas_int > 100:
        print("Lütfen mantıklı bir değer giriniz.")
        exit()
    else:

    # DONE[4]: yaşa göre kategori belirleyin:
    # 0-12: "Çocuk", 13-19: "Genç", 20-64: "Yetişkin", 65+: "Yaşlı"
        if yas_int < 13:
            kategori = "Çocuk"
        elif yas_int < 20:
            kategori = "Genç"
        elif yas_int < 65:
            kategori = "Yetişkin"
        else:
            kategori = "Yaşlı"
    

    # DONE[5]: Sadece kategori çıktısını yazdırın
    print("Yaşınız: ", yas_int, " ", "Kategori: ", kategori)
