#sets

nominal = (1,3,5,10,20,50,100,200,500,1000, 2000,5000)
person = ('nothing', 'nothing', 'nothing', 'nothing', 'T.Moldo',
          'K.Datka', 'T.Satylganov', 'A.Osmonov', 'S.Karalaev', 
          'J.Balasagyn', 'Manas', 'S.Chokmorov')

money = dict(zip(nominal, person))

for k,v in money.items():
    print(f'{k}-{v}')

print(money)