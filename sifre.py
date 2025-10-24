# nAİm
# 24.10.2025

# doğru şifreyi belirliyoruz
dogru_sifre = "1234"

# sayaç sıfırdan başlar
hak = 3

while hak > 0:
    girilen = input("Şifrenizi girin: ")

    if girilen == dogru_sifre:
        print("Giriş başarılı! Hoş geldiniz.")
        break
    else:
        hak -= 1
        print("Yanlış şifre!")
        if hak > 0:
            print(f"Kalan deneme hakkınız: {hak}")
        else:
            print("Hesap kilitlendi!")

