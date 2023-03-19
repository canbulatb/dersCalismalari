#Kullanıcının tuttuğu 1 ile 10 arasındaki sayıyı taymin eden bir oyun yapınız
import random

print("Lütfen 1 ile 10 arasında bir sayı tutunuz")
sayi=5
altLimit=1
ustLimit=10
sonuc=input("Tuttuğunuz sayı "+str(sayi)+" mi, Büyük mü, küçük mü d,b,k")
while 1==1:
    sonuc=input("Tuttuğunuz sayı "+str(sayi)+" mi, Büyük mü, küçük mü d,b,k")
    if sonuc=="d":
        print("Sonuç doğru. Çok güzel")
        break
    elif sonuc=="b":
        altLimit=sayi+1
        sayi=random.randint(altLimit,ustLimit)
    elif sonuc=="k":
        ustLimit=sayi-1
        sayi=random.randint(altLimit,ustLimit)



