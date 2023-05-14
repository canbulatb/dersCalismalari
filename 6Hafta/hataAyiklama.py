balance=2
degerB=True
while True:
    deger=input("lütfen yatıracağınız payayı giriniz...: ")
    for i in deger:
        if i not in ("0123456789"):
            print("Lütfen düzgün veri giriniz...: ")
            degerB=False
            break
    if degerB==True:
        break
balance+=int(deger)
print(balance)
        
    
    

balance
