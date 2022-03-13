anahtar = input('Anahtarı girin (Yalnızca İngilizce karakter kullanın, boşluk bırakmayın) : \n' + '--->')
harfler = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
kare = ''
mesaj = input('Mesajı girin (Yalnızca İngilizce karakter kullanın, boşluk bırakmayın) : \n' + '--->')
sifreliMesaj = ''

for i in(anahtar):
    a = len(kare)
    if((a+1)%6 == 0):
        kare += ';'
    if(i not in kare):
        kare += i


for j in(harfler):
    a = len(kare)
    if((a+1)%6 == 0):    
        kare += ';'
    if(j not in kare):
        kare += j

kare += ';'

if(mesaj[0] == 'j'):
    mesaj[0]='i'


for i in range(len(mesaj)-1):
    if(mesaj[i+1]=='j'):
        mesaj[i+1] = 'i'
    if(mesaj[i] == mesaj[i+1]):
        mesaj = mesaj[:i+1] + 'x' + mesaj[i+1:]
        

if(len(mesaj)%2 == 1):
    mesaj += 'x'


for k in range(0,len(mesaj),2):
    satira = kare.index(mesaj[k])//6
    satirb = kare.index(mesaj[k+1])//6
    sutuna = kare.index(mesaj[k])-satira*6
    sutunb = kare.index(mesaj[k+1])-satirb*6

    if(satira != satirb and sutuna != sutunb):
        sifreliMesaj += (kare[satira*6+sutunb] + kare[satirb*6+sutuna])
    elif(satira != satirb):
        sifreliMesaj += (kare[((satira+1)*6+sutuna)%30] + kare[((satirb+1)*6+sutunb)%30])
    else:
        sifreliMesaj += (kare[(satira*6+((sutuna+1)%5))] + kare[(satirb*6+((sutunb+1)%5))])

print(sifreliMesaj)        

