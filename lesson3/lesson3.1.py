names = ['Vanya', 'Konstantin', 'Dean', 'Sam', 'Sam']
ages = [12, 33, 55, 77]

ages.extend(names)

ages.append(names.pop(2))

print(ages)
print(names)

print(names.count('Sam'))
print(names.index('Sam'))
