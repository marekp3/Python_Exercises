
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

polaczenia = [(a,b) for a in ports for b in ports]
print(polaczenia)
print(len(polaczenia))


polaczenia = [(a,b) for a in ports for b in ports if a!=b]
print(polaczenia)
print(len(polaczenia))

polaczenia = [(a,b) for a in ports for b in ports if a < b]
print(polaczenia)
print(len(polaczenia))


