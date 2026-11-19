#lisaülesanne
try:
    print("Vali programm:")
    print("1 - Arvu kontroll")
    print("2 - Kehamassiindeks")
    print("3 - Ostu allahindlus")
    valik = input("Sisesta valik (1-3): ")
except ValueError: 
    print("Viga valik.")
    


print("Arvu kontroll")
try:
    arv=int(input("Sisesta täisarv: ")) #'  =>  "
    if arv>0: #pärast 0 on :
        print("Arv on positiivne")
    if arv==0: #else if arv=0:  =>  if arv==0:
        print("Arv on null")
    if arv<=0: #lisasin see rida, else: kustutasin ära
        print("Arv on negatiivne")
    if arv%2==0:
        print("Arv on paarisarv")
    else:
        print("Arv on paaritu")
    if arv/3: #lisaülesanne
        print("Arv jagub 3-ga")
    else:
        print("Arv ei jagu 3-ga")
except ValueError: #lisasin try ja except ValueError
    print("Palun sisesta ainult numbrid.")



print()
print("Kehamassiindeks: ")
try:
    mass=float(input("Sisesta kaal (kg): "))
    if mass<=0:
        print("Palun sisesta ainult positiivsed numbrid.") #lisaülesanne
    mass=float(input("Sisesta kaal (kg): "))
    pikkus=float(input("Sisesta pikkus (m): ")) #lisasin veel üks )
    if pikkus<=0:
        print("Palun sisesta ainult positiivsed numbrid.")
    pikkus=float(input("Sisesta pikkus (m): "))
    kmi=mass/pikkus*2 
    print("KMI:", round(kmi,1))
    if kmi<18.5:
        print("Alakaal")
    elif kmi>=18.5:
        print("Normaalkaal")
    elif kmi>=25:
        print("Ülekaal")
    elif kmi>=30: #lisasin :
        print("Rasvumine")
except ValueError: #lisasin try ja except ValueError
    print("Palun sisesta ainult numbrid.")



print()
print("Ostu allahindlus")
try:
    summa=float(input("Sisesta ostusumma: "))
    if summa<0: #kustutasin = ära
        print("Vigane summa")
    elif summa>100 or summa<=500:
        print("Allahindlus 5%, maksta:", round(summa*0.95,2))
    elif summa>500:
        print("Allahindlus 10%, maksta:", round(summa*0.9,2))
    else: #lisasin :
        print("Allahindlust pole, maksta:"), summa #lisasin :
except ValueError: #lisasin try ja except ValueError
    print("Palun sisesta ainult numbrid.")