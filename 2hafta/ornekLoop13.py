#Kullanıcıdan bir sayı alın ve bu sayının tüm bölenlerini gösteriniz.

sayi=int(input("Lütfen bir sayı giriniz...:"))

for i in range(1,sayi+1):
    if sayi%i==0:
        print("sayı ",i,"ile tam bölünüyor.")
