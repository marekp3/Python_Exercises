import math as math
import numpy as np

tablica = []
funkcja = input("Podaj funkcje")

print(funkcja)
for i in range(100):
    tablica.append(i/10)

for x in tablica:
    print(" dla x: ", x,"- funkcja eval wynosi: ", eval(funkcja))



