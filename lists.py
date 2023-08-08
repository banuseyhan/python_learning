# js de array olarak tanımladığımız py de list olarak tanımlanır
msg = "life is too short for learning german" .split ()

print (msg[0][0]) 
#liste olduğu için ilk array life ama ikinci array l yi temsil eder
sayilar = [1,3,5,7,9]

sonuc = sayilar
sonuc = sayilar[0]
sonuc = sayilar[4]
# sonuc = sayilar[5] # IndexError: list index out of range

isimler = ['ahmet','ali',' can','ada']

sonuc = isimler[0]

# print(type(isimler[0]))
# print(type(sayilar[0]))

listeAli = ['ali',20]
listeAhmet = ['ahmet',22]

sonuc = listeAli[0]
sonuc = listeAli[1]

# ogrenciler = [["ali",20],["ahmet",22]]
ogrenciler = [listeAli,listeAhmet]

sonuc = ogrenciler[0][0]
# sonuc = ogrenciler[1][0]

print(sonuc)



diller = ["Python","C#","Java","Javascript","React"]

sonuc = diller
sonuc = type(diller)
sonuc = diller[0:2]
sonuc = diller[2:]
sonuc = diller[:3]
sonuc = diller[-1]
sonuc = diller[-4:-1]
# diller[0] = "Html"
diller[-1] = "Html"
sonuc = len(diller)
sonuc = diller + ["Angular","Vuejs"]

# if bloğu=> Koşul ifadeleri
if "Python" in diller:
    print("değer listenin bir elemanı")

# döngüler
for x in diller:
    print(x)

del diller[0]

sonuc = diller

print(sonuc)
