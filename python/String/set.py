collection = {1, 2, 3, 4, 4 ,5, "Hello World"}
print(collection.pop())

deal = set()

deal.add(1)
deal.add(2)
deal.add("Pokharar")
deal.add((1, 2, 3)) #method
deal.remove((1,2, 3)) #method
deal.clear() #method

print(deal)

set1 = {1, 2 ,3, 3 ,4}
set2 = {4, 2, 5}

print(set1.union(set2))
print(set1.intersection(set2))

#collection = {} #empty dictionary
#collection = set() # empty set
