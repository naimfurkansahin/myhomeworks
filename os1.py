#nAİm
#26.10.2025
#class ile basit obs

class Ogrenci:
    def __init__(self, ad, soyad, numara, not_ortalamasi):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.not_ortalamasi = not_ortalamasi

    def bilgi_goster(self):
        print(f"Ad: {self.ad}, Soyad: {self.soyad}, Numara: {self.numara}, Ortalama: {self.not_ortalamasi}")

    def basarili_mi(self):
        if self.not_ortalamasi >= 50:
            print("Geçti")
        else:
            print("Kaldı")


ogr1 = Ogrenci("Furkan", "Şahin", 252301034, 90)
ogr2 = Ogrenci("İlknur", "Üzüm", 121415172, 45)

ogr1.bilgi_goster()
ogr1.basarili_mi()

print()

ogr2.bilgi_goster()
ogr2.basarili_mi()
