#Kullanıcıdan bir sayı alın ve aldığınız sayının listedeki
#sayıdan büyük, küçük veya eşit olduğunu gösteriniz. 

listem=[19,34,62,93]
sayi=int(input("Lütfen bir sayı giriniz...: "))

for x in listem:
    if sayi>x:
        print(sayi,x,"ten büyük")
    elif sayi<x:
        print(sayi,x,"ten küçük")
    else:
        print(sayi,x,"e eşittir. ")