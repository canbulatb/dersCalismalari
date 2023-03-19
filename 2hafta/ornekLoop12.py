#1 ile 100 sayıları arasında hem 3 e hem de 4 e bölünebilen sayıları gösteriniz

for i in range(101):
    if i%3==0 and i%4==0:
        print(i)