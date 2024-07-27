from random import shuffle

# Kart sınıfı, her bir kartın tipini ve değerini tutar.
class Kart:
    def __init__(self, tip, deger):
        self.tip = tip
        self.deger = deger

    # Kart sınıfının temsilini string olarak döndürür.
    def __repr__(self):
        return f"{self.tip} {self.deger}"

# Deste sınıfı, 52 karttan oluşan bir kart destesini temsil eder.
class Deste:
    tipler = ["karo", "sinek", "kupa", "maça"]  # Kart tipleri
    degerler = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]  # Kart değerleri

    def __init__(self):
        # Tüm kartları oluşturur.
        self.kartlar = [Kart(tip, deger) for tip in Deste.tipler for deger in Deste.degerler]

    # Destede kalan kart sayısını döndürür.
    def kartSayisi(self):
        return len(self.kartlar)

    # Kartları karıştırır, ancak destede eksik kart varsa hata verir.
    def kartlariKaristir(self):
        if self.kartSayisi() < 52:
            raise ValueError("Deste bozulmadan kartları karıştırabilirsiniz.")
        shuffle(self.kartlar)

    # Belirtilen sayıda kart dağıtır.
    def kartDagit(self, adet):
        kartSayisi = self.kartSayisi()
        if kartSayisi == 0:
            raise ValueError("Bütün kartlar dağıtıldı.")
        adet = min([kartSayisi, adet])
        kartlar = self.kartlar[-adet:]
        self.kartlar = self.kartlar[:-adet]
        return kartlar

    # Bir adet kart dağıtır.
    def kartAt(self):
        return self.kartDagit(1)[0]

# Deste oluşturulur.
deste1 = Deste()

# Kartlar karıştırılır.
deste1.kartlariKaristir()

# Bir kart çekilir ve yazdırılır.
print(deste1.kartAt())

# Beş kart dağıtılır ve yazdırılır.
print(deste1.kartDagit(5))

# Kalan kartlar yazdırılır.
print(deste1.kartlar)

# Kalan kart sayısı yazdırılır.
print(deste1.kartSayisi())

# Üç kart daha dağıtılır ve yazdırılır.
print(deste1.kartDagit(3))

# Güncellenmiş kart sayısı yazdırılır.
print(deste1.kartSayisi())

# Kalan kartlar yazdırılır.
print(deste1.kartlar)
