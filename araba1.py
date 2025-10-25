#nAİm
#26.10.2025
#class alıştırması

class Araba:
    def __init__(self, marka, model,yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.yakit = 100

    def bilgi_goster(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}, Yakıt: {self.yakit}")

    def sur(self, km):
        gereken_yakit = (km / 10) * 5

        if self.yakit <= 0:
            print("Yeterli yakıt yok!")
        elif gereken_yakit > self.yakit:
            print("Yeterli yakıt yok! Lütfen yakıt ekleyin.")
        else:
            self.yakit -= gereken_yakit
            print(f"Araba {km} km sürüldü. Kalan yakıt: {self.yakit}")

    def yakit_ekle(self, miktar):
        if self.yakit + miktar > 100:
            self.yakit = 100
            print("Depo doldu!")
        else:
            self.yakit += miktar
            print(f"Yakıt eklendi. Yeni seviye: {self.yakit}")


araba1 = Araba("BMW", "e60", 2008)

araba1.bilgi_goster()

print()

araba1.sur(250)
araba1.bilgi_goster()

print()

araba1.yakit_ekle(50)
araba1.bilgi_goster()