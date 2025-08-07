import random
islemler = ["+","-","*","/"]
islem_sayisi = 0
dogru = 0
def cikarma():
    a = random.randint(1,100)
    b = random.randint(1,a)
    soru = input(str(a) +"-" +str(b) +" nin cevabı nedir : ")
    cevap = int(soru)
    if cevap ==  a-b :
        print("doğru")

    elif cevap != a-b :
        print("yanlış")

def toplama():
    a = random.randint(1,100)
    b = random.randint(1,100)
    soru = input(str(a) +"+" +str(b) +" nin cevabı nedir : ")
    cevap = int(soru)
    if cevap ==  a+b :
        print("doğru")

    elif cevap != a+b :
        print("yanlış")

def carpma():
    a = random.randint(1,20)
    b = random.randint(1,20)
    soru = input(str(a) +"*" +str(b) +" nin cevabı nedir : ")
    cevap = int(soru)
    if cevap ==  a*b :
        print("doğru")

    elif cevap != a*b :
        print("yanlış")

def bolme():
    a = random.randint(1, 100)
    b = random.randint(1, a)
    while a % b != 0 :
        a = random.randint(1, 100)
        b = random.randint(1, a)

    soru = input(str(a) +"/" +str(b) +" nin cevabı nedir : ")
    cevap = int(soru)
    if cevap ==  a/b :
        print("doğru")

    elif cevap != a/b :
        print("yanlış")
while islem_sayisi != 20 :
    islem = random.choice(islemler)
    islem_sayisi = islem_sayisi + 1
    print("Soru " +str(islem_sayisi))
    if islem == "-":
        cikarma()
    if islem == "+":
        toplama()
    if islem == "*":
        carpma()
    if islem == "/":
        bolme()



