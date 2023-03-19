#Girilen metinin harflerini alt alta yazdırınız. 
#while ile 
# ve for ile

metin=input("Bir metin giriniz:")
print("for ile...")
for i in metin:
    print(i)

i=0
print("while ile...")
while i<len(metin):
    print(metin[i])
    i+=1
