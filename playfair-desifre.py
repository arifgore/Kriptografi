anahtar = input('Anahtarı girin (Yalnızca İngilizce karakter kullanın, boşluk bırakmayın) : \n' + '--->')
harfler = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
kare = ''
sifreliMesaj = input('Şifreli mesajı girin (Yalnızca İngilizce karakter kullanın, boşluk bırakmayın) : \n' + '--->')
mesaj = ''

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


for k in range(0,len(sifreliMesaj),2):
    satira = kare.index(sifreliMesaj[k])//6
    satirb = kare.index(sifreliMesaj[k+1])//6
    sutuna = kare.index(sifreliMesaj[k])-satira*6
    sutunb = kare.index(sifreliMesaj[k+1])-satirb*6

    if(satira != satirb and sutuna != sutunb):
        mesaj += (kare[satira*6+sutunb] + kare[satirb*6+sutuna])
    elif(satira != satirb):
        mesaj += (kare[((satira-1)*6+sutuna)%30] + kare[((satirb-1)*6+sutunb)%30])
    else:
        mesaj += (kare[(satira*6+((sutuna-1)%5))] + kare[(satirb*6+((sutunb-1)%5))])

print(mesaj)        

