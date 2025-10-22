'''
yazan : nAİm
16.10.2025
    bu ödevimde liste ve for döngüleri kullanarak arayüzlü bir üye kayıt uygulaması
    hazırlayacağım.
'''

if __name__ == "__main__":

    baslik = "Üye Kayıt Sistemi"

    uye_adlari = []
    uye_soyadlari = []
    uye_numaralari = []

    print("-"*100)
    print(f"| {baslik:^94} |x|")
    print("-"*100)

    uye_sayisi = int(input("Kaç üye kaydedeceksiniz?: "))

    for sıra in range(uye_sayisi):
        uye_adlari.append(input(f"{sıra+1} . Üye adını giriniz: "))
        uye_soyadlari.append(input(f"{sıra+1} . Üye soyadını giriniz: "))
        uye_numaralari.append(input(f"{sıra+1} . Üye numarasını giriniz: "))

    print("-"*100)
    print(f"| {"No":^8} | {"İsim":<30} | {"Soyisim":<30} | {"Numara":<20}|")
    print("-"*100)

    for sıra in range(uye_sayisi):
        print(f"| {sıra+1:^8} | {uye_adlari[sıra]:<30} | {uye_soyadlari[sıra]:<30} | {uye_numaralari[sıra]:<20}|")

    print("-"*100)