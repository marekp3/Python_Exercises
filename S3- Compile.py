import math
import time

argument_list = []
for i in range(10000):
    argument_list.append(i/10)
#----------------------------------------
formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

results_list = []
start = time.time()
for x in argument_list:
    results_list.append((eval(formulas_list[0]),eval(formulas_list[1])))
stop = time.time()
total = stop - start
print("calculating two eqiations:\n 1: ", formulas_list[0], "\n 2: ", formulas_list[1])
print("took: ", total)

formulas_list_compiled = [compile(formulas_list[0],'interna','eval'),compile(formulas_list[1],'interna','eval')]

results_list = []
start = time.time()
for x in argument_list:
    results_list.append((formulas_list_compiled[0], formulas_list_compiled[1]))
stop = time.time()
total = stop - start
print("calculating two eqiations:\n 1: ", formulas_list[0], "\n 2: ", formulas_list[1])
print("took: ", total)

