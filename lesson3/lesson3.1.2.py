people = ['Mary', 'Bobby', 'Dean', 'Mas', 'John', 'Kas', 33, 44,11,23.4, False]
names = []
ages = []

for i in people:
    if type(i) == str:
        names.append(i)
    else:
        ages.append(i)

ages.remove(False)
ages.sort()
names[3] = 'Sam'
names.reverse()
print(names)
print(ages)