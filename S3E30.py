listA = list(range(1,6))
listB = list(range(1,6))

#Solution1

"""
product = []
for a in listA:
    for b in listB:
        product.append((a,b))
print(product)
"""

#Solution2

product = [(a,b) for a in listA for b in listB if a % 2 and b % 2]
print(product)