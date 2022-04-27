sayı = int(input("Bir Sayı Giriniz: "))

i = 1
toplam = 0
while (i < sayı):
    if (sayı % i == 0):
        toplam += i
    i += 1

if (toplam == sayı):
    print(sayı,"Mükemmel bir sayıdır.")
else:
    print(sayı,"Bu bir mükemmel sayı değildir.")