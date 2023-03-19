#3 Kullanıcının adını, soyadını ve yaşını alınız.
# Bunları format metodu ile yazırınız. While kullanarak.
i=0
liste=[]
while i<3:
    isim=input("isminizi giriniz:")
    soyisim=input("Soyisminizi giriniz:")
    yas=input("Yaşınızı giriniz.")
    print("isminiz{}, Soyisminiz {}, Yaşınız{}".format(isim,soyisim,yas))
    i=i+1
