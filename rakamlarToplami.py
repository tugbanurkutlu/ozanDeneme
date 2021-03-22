sayi=int(input("sayininizi giriniz: "))
toplam=0
while(sayi>0):
    birlerBasamagi=sayi%10
    toplam+=birlerBasamagi
    sayi=sayi//10
print(toplam)