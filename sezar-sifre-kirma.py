harfler = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sifreli = input('Deşifrelenecek mesajı girin: \n' + '--->')
listDesifreli = []
flag = False
for artim in range(26):
    desifreli = ''
    for j in(sifreli):
        if(harfler.index(j)<artim):
            desifreli += harfler[harfler.index(j)+26-artim]
        else:
            desifreli += harfler[harfler.index(j)-artim]
    listDesifreli.append(desifreli)

for i in(listDesifreli):
    if('the' in i or 'and' in i or 'you' in i or 'dont' in i or 'does' in i or 'will' in i or 'not' in i):
        print(i)
        flag=True

if(not flag):
    print('Doğru sonucu tespit edemedik, belki kendiniz göz atmak istersiniz:\n')
    for i in(listDesifreli):
        print(i+'\n')
