#range
seq = range(5)

for i in seq:
    print(i)

#range(stop)
for x in range(5): 
    print(x)

#range(start, stop)
for y in range(2, 10): 
    print(y)

#range(start, stop, step)
for z in range(2, 10, 2): 
     print(z)

#odd even in range
for odd in range(1, 50, 2):
    print(odd)

for even in range(2, 50, 2):
    print(even)

#pass statement
for i in range(5):
    pass
if i > 5:
    pass
print("Use for for future code.")