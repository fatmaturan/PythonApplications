def not_hesapla(satir):
    satir = satir.strip()  
    liste = satir.split(':')

    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if 90 <= ortalama <= 100:
        harf = "AA"
    elif 85 <= ortalama < 90:
        harf = "BA"
    elif 80 <= ortalama < 85:
        harf = "BB"
    elif 75 <= ortalama < 80:
        harf = "CB"
    elif 70 <= ortalama < 75:
        harf = "CC"
    elif 65 <= ortalama < 70:
        harf = "DC"
    elif 60 <= ortalama < 65:
        harf = "DD"
    elif 50 <= ortalama < 60:
        harf = "FD"
    else:
        harf = "FF"

    return f"{ogrenciAdi}: {harf}\n"


def ortalamalari_oku():
    # Dosyayı oku ve her satırı işle
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))  # Hesaplanan notu yazdır


def not_gir():
    # Kullanıcıdan bilgileri al
    ad = input('Öğrenci adı: ')
    soyad = input('Öğrenci soyad: ')
    not1 = input('Not 1: ')
    not2 = input('Not 2: ')
    not3 = input('Not 3: ')

    # Bilgileri dosyaya yaz
    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(f"{ad} {soyad}:{not1},{not2},{not3}\n")


def notlari_kaydet():
    with open('sinav_notlari.txt', "r", encoding="utf-8") as file:
        liste = [not_hesapla(satir) for satir in file]

    with open("sonuclar.txt", "w", encoding="utf-8") as file2:
        file2.writelines(liste)


# Ana döngü: Kullanıcıdan işlem seçmesini iste
while True:
    islem = input('1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n')

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kaydet()
    elif islem == '4':
        break
    else:
        print("Geçersiz işlem. Lütfen tekrar deneyin.")
        break