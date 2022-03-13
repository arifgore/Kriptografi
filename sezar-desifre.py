harfler = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sifreli = input('Deşifrelenecek mesajı girin: \n' + '--->')
artim = int(input('Anahtar değerini girin: \n' + '--->'))%26
desifreli = ''

for j in(sifreli):
    if(harfler.index(j)<artim):
        desifreli += harfler[harfler.index(j)+26-artim]
    else:
        desifreli += harfler[harfler.index(j)-artim]

print(desifreli)

