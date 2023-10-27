import string
import random

A = string.ascii_letters

n = 3
for i in range(n):
    L = []
    for j in range(n):
        L.append(random.choice(A))
    for element in L:
        print(element, end='\t')
    print() 