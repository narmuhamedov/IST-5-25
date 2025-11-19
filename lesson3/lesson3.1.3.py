#Кортежи
money = (1, 3, 5, 10, 20, 50, 100, 200, 500, '1k')
money = list(money)
money.append('2k')
money.append('5k')

money = tuple(money)
print(money)

world = list('hello any one how are you')
world.reverse()
print(world)