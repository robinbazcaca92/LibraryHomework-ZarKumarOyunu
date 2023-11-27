from random import randrange

# Zar Oyunu, girdiğiniz sayı zar sayısı aynı ise bakiyeniz 2x olur
# 1 eksik ise yani zar 3 iken siz 2 veya 4 demişseniz yaklaştığınız için paranız iade olur
# eğer 2 eskik ise bahisin %25' ini iade alırsınız %75i kaybolur
# 1.000 Bakiyeyi 10.000 yapan kazanır. 50' den a
# detaylar dikkate alınmamıştır.

bakiye =1000

while bakiye>=0:
    print("Güncel Bakiyeniz", bakiye)
    zaryüz = randrange(1, 7)
    tahmin = input("Tahmin ettiğiniz sayiyi giriniz: ")

    if int(tahmin) > 6 or int(tahmin) < 0:
        print("Zarda böyle bir sayı yok!")
        break

    bahis = int(input("Bahis miktarını giriniz: "))

    if bahis > bakiye:
        print("Yetersiz Bakiye!")
        break



    if int(tahmin) == zaryüz:
        bakiye= bakiye + (2*int(bahis))
    elif int(tahmin) == zaryüz - 1:
        bakiye = bakiye
    elif int(tahmin) == zaryüz - 1:
        bakiye = bakiye
    elif int(tahmin) <= zaryüz - 2:
        bakiye = bakiye - (int(bahis) * 0.75)
        bakiye = int(bakiye)
    elif int(tahmin) >= zaryüz - 2:
        bakiye = bakiye - (int(bahis) * 0.75)
        bakiye = int(bakiye)

    print("Gelen Rakam:",zaryüz)
    print("Güncel Bakiyeniz",bakiye)
    if bakiye == 10000:
        print("Tebrikler tam bir kumarbazsınız")
    elif bakiye <= 0:
        print("Yetersiz Bakiye!")
        break

