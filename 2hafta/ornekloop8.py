#bir rakamın çarpım tablosunu gösteriniz. 

sayi=int(input("Lütfen çarpım tablosu oluşturulacak bir sayı giriniz...:" ))

for i in range(1,11):
    print(sayi,"x",i,"=",i*sayi)
