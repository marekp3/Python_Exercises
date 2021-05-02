"""
listA = list(range(6))
listB = list(range(6))

print(listA)
print(listB)

product = ((a,b) for a in listA for b in listB if a%2 and b%2)

while True:
    try:
        next(product)
    except StopIteration:
        print(" all generator values have been printed")
        break

"""

#Laboratorium
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

polaczenie_0 = ((a,b) for a in ports for b in ports)
i = 0
while True:
    try:
        print(next(polaczenie_0), end='')
        i+=1
    except StopIteration:
        print('\n',"Ilosc polaczen to: ", i)
        i=0
        break

polaczenie_1 = ((a,b) for a in ports for b in ports if a!=b)
while True:
    try:
        print(next(polaczenie_1), end='')
        i+=1
    except StopIteration:
        print('\n',"Ilosc polaczen to: ", i)
        i=0
        break




polaczenie_2 = ((a,b) for a in ports for b in ports if a < b)
while True:
    try:
        print(next(polaczenie_2), end='')
        i+=1
    except StopIteration:
        print('\n',"Ilosc polaczen to: ", i)
        i=0
        break