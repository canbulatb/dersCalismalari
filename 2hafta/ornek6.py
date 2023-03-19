#üç satı alın ve bu sayılarının medyanını bulunuz. 
sayi1=int(input("1. Sayıyı giriniz...: "))
sayi2=int(input("2. Sayıyı giriniz...: "))
sayi3=int(input("3. Sayıyı giriniz...: "))
#a,b,c sayıları (b<a<c or c<a<b)
if sayi2<sayi1<sayi3 or sayi3<sayi1<sayi2:
    print(str(sayi1) + "Medyandır")
elif sayi1<sayi2<sayi3 or sayi3<sayi2<sayi1:
    print(str(sayi2) + "Medyandır")
else:
    print(str(sayi3)+" Medyandır")
