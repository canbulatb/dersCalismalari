import random
class Client:
    bankName="AMR BANK"
    interestRate=1.14
    numClient=0
    totalBalance=0
    def __init__(self,name,surname,bakiye,cocuk=0,gender="Uncertain"): #ilk çalışan fonksiyon. Burada tüm tanımlamalar yapılıyor.
        #print("class oluşturuldu...")
        self.name=name #self.name adında bir değişken oluşturuldu ve name bune eşitlendi.
        self.surname=surname
        self.balance=bakiye #self.balance adında bir değişken oluşturuldu ve bakiye  bune eşitlendi.
        self.email=f"{name}.{surname.lower()}@gmail.com"#name+"."+surname+"@gmail.com" #isim ve soiyim alındı ve email adında yeni bi atribute oluşturuldu.        
        if gender in "MFmf" and len(gender)==1:
            self.gender=gender.upper()
        else: 
            self.gender="Uncertain"
        self.accountNumber=f"ABN{random.randint(10000000,999999999)}" #ABN+str(random.randint(10000000,999999999))
        self.cocuk=cocuk
        if self.cocuk>0:
            self.cocukSayisi()
        Client.totalBalance+=self.balance
        Client.numClient+=1
        
        
    def cocukSayisi(self):
        self.balance+=250*self.cocuk
        print("Çocuk parası eklendi.")
       
    
    def paraYatir(self,balance):
        self.balance+=balance
        print(f"Sayin {self.name}, {balance} Para yatırıldı. Bakiye :",self.balance)
        
    def paraCek(self,balance):
        self.balance-=balance
        print(f"Sayin {self.name}, {balance} Para çekildi. Bakiye :",self.balance)                

    def rentCikar(self):
        self.balance-=self.rent
        print(f"Sayin {self.name}, {self.rent} kiraya verildi.. Bakiye :",self.balance) 

    def sendMoney(self,account,money):
        basarili=False
        clients=[obj for obj in globals().values() if isinstance(obj,Client)]
        x=0
        for x in clients: 
            if x.accountNumber==account and self.accountNumber!=x.accountNumber:
                    x.balance+=money
                    self.balance-=money
                    print("Para aktarımı başarılı")
                    print(f"{money} puan {self.name} den {x.name} ye gönderildi.")
                    basarili=True
                    break
        if not basarili:
            print("Aktarılacak hesap bulunamadı. ")
                            
c1=Client("omer","uygur",5000,3,"M")
c2=Client("Bilal","Can",3000,2,"M")
c3=Client("Fatma","Can",7000,2,"M")
print(c1.email)
c1.has_child=False #attribute dışarıda tanımlanabiliyor. 
print(c1.gender)

c1.paraYatir(1000) #1000 para yatırıldı.
c1.paraCek(2000) #2000 para çekildi.

#dışarıda rent isminde attribute oluşturup 
#bir metot oluşturup bu renti balance'den çıkar.
c1.rent=300
c1.rentCikar()
#accountNumber oluştur random fonksiyonu kullanılacak ve istenilen formatta hesap numarası oluşturulacak. 

print(c1.accountNumber)
#Her müşteride çocuk sayısı alacağız çocuk başına 250 ekstra puan verecek.

#clients=[obj for obj in globals().values() if isinstance(obj,Client)]

#sendMoney diye bir method oluşturulacak. Bir müşteriden diğerine para aktarılacak
#sendMoney'in iki parametre alacak. biri AccountNummet diğeri amount
#c1.sendMoney(account,300)
print(f"{c1.name} bakiye {c1.balance}")
print(f"{c2.name} bakiye {c2.balance}")
print(f"{c3.name} bakiye {c3.balance}")
c2.sendMoney(c3.accountNumber,1000)
print(f"{c1.name} bakiye {c1.balance}")
print(f"{c2.name} bakiye {c2.balance}")
print(f"{c3.name} bakiye {c3.balance}")
print(c1.interestRate)

Client.interestRate=1.2
print(Client.interestRate)
print(c1.interestRate)

# @classmethod
# def clasmetodu():
#     pass

# @staticmethod
# def statikmedotu():
#     pass

class Premiumclient(Client):
    def __init__(self, name, surname, bakiye,cocuk=0, gender="Uncertain"):
        super().__init__(name, surname, bakiye, cocuk, gender)
        self.loyaltyPoint=0
        self.ekstra=False
        
    def paraYatir(self, balance):
        loyaltyEkstra=balance//10
        print("ekstra :", loyaltyEkstra)
        self.loyaltyPoint+=loyaltyEkstra
        if self.loyaltyPoint>50 and self.ekstra==False:
            self.balance+=10
            self.ekstra=True
        return super().paraYatir(balance)
    
    
    def sendMoney(self, account, money):
        
        return super().sendMoney(account, money)
    
    

p1=Premiumclient("Fatih","Kaya",10000,2,"M")
p1.loyaltyPoint
print(p1.balance)
print(p1.loyaltyPoint)
p1.paraYatir(1000)
print(p1.balance)
print(p1.loyaltyPoint)


# VIP klas oluşturacağız. clientden inheritance alacak.
# VIP class 2 tane level olacak. Bronz, silver ve gold
# Vip class para yaptıma yapacağı zaman levellerine göre ekstra para alacak. 
# Bronz için *0.01, silver 0.02 gold için 0.03
# her yeni musteri bronz levelinden başlayacak. 
# 10 para yatırma işleminde 1 level atlanacak. ,

class VIP(Client):
    def __init__(self, name, surname, bakiye,cocuk=0, gender="Uncertain"):
        super().__init__(name, surname, bakiye, cocuk, gender)
        self.level="Bronz"
        self.ekstraCarpan=0.01
        self.paraYatirmaSayisi=0
    
    def paraYatir(self, balance):
        self.levelBelirle()
        balance+=balance*self.ekstraCarpan
        return super().paraYatir(balance)
    
    def levelBelirle(self):
        self.paraYatirmaSayisi+=1
        if self.paraYatirmaSayisi>20 :
            self.level="Gold"
            self.ekstraCarpan=0.03    
        elif self.paraYatirmaSayisi>10:
            self.level="Silver"
            self.ekstraCarpan=0.02    

v1=VIP("Ahmet","Kaya",10000,2,"M")

print(v1.name,v1.level)

for i in range(20):
    v1.paraYatir(100)

print(v1.name,v1.level)
print(v1.paraYatirmaSayisi)

def __len__(self):
    return self.name

print (c1.__dict__)