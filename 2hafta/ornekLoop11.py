import random


i=0
tahminSayi=random.randint(0,100)
altLimit=1
ustLimit=10
while 1==1:
    sayi=int(input("Lütfen bir sayı giriniz...:"))
    if sayi==0:
        break
    elif tahminSayi==sayi:
        print(i,"seferde doğru bildiniz.")
        break
    elif tahminSayi>sayi:
        print("tahmin sayısı daha büyük")
    elif tahminSayi<sayi:
        print("tahmin sayısı daha küçük")
    i+=1
    
    