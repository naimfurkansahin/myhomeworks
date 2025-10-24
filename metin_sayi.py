# nAİm
# 16.10.2025
# herhangi bir metindeki en çok tekrar eden kelimeleri bulmak.


if __name__ == "__main__":
 from collections import Counter
 import re

# metni buraya yazabilirsin
 metin = """
METİN BURAYA GELECEK
"""

# metni küçük harfe çevir
 metin = metin.lower()

# noktalama işaretlerini kaldır
 metin = re.sub(r"[^\w\s]", "", metin)

# kelimelere ayır
 kelimeler = metin.split()

# kelimeleri say
 sayim = Counter(kelimeler)

# en çok geçen 10 kelimeyi bul
 en_cok = sayim.most_common(10)

# sonuçları yazdır
 print("En çok geçen kelimeler:")
 for kelime, adet in en_cok:
    print(f"{kelime}: {adet}")
