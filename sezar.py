harfler = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mesaj = input('Şifrelenecek mesajı girin (Yalnızca İngilizce karakterler kullanın, boşluk bırakmayın):\n' + '--->' ).lower()
sifreli = ''
artim = int(input('Anahtar değerini girin: \n' + '--->'))%26

for i in(mesaj):
    sifreli +=harfler[(harfler.index(i)+artim)%26] 
    
print(sifreli)

