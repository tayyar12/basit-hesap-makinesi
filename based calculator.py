




while True:


 sayi1 = int(input("sayı gir: "))
 sayi2 = int(input("sayı gir: "))

 def toplama (sayi1 , sayi2):
    toplamasonuc = sayi1 + sayi2
    print(f"{sayi1} + {sayi2} = {toplamasonuc}")

 def cıkarma (sayi1 , sayi2):
    cikarmaislemko = sayi1 - sayi2
    print(f"{sayi1} - {sayi2} = {cikarmaislemko}")
 def carpma (sayi1 , sayi2):
    carpmaislem = sayi1 * sayi2
    print(f"{sayi1} + {sayi2} = {carpmaislem}")

 def bolme (sayi1 , sayi2):
    bolmeislem = sayi1 / sayi2
    print(f"{sayi1} + {sayi2} = {bolmeislem}")

 istek = input("ne istersiniz:")


 if istek == "toplama":
    toplama(sayi1 , sayi2)
    

 elif istek == "çıkarma":
    cıkarma(sayi1,sayi2)

 elif istek == "çarpma":
    carpma(sayi1,sayi2)

 elif istek == "bölme":
    bolme(sayi1,sayi2)

 else:
    print("anlamadım")
    break
