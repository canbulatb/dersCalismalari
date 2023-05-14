balance=2
while True:
    try:
        amonut=int(input("Yatırılacak miktar: "))
        if amonut<=0:
            raise ArithmeticError("Girilen miktar negatif olamaz")
        balance+=amonut
        print("Bakiyeniz: ", balance)
           
        devam=input("Devam etmek istiyormusunuz: (E/H)").upper()
        if devam in["H","E","EVET","HAYIR"]:
            break
    except ArithmeticError as e:
        print(e)
    except ValueError as e:
        print("Lütfen pozitif bir miktar giriniz.")
    except:
        print("Hata oluştu.")
    else:
        print("Bakiyeniz: ", balance)

