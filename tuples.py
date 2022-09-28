#python programme to find size of a tuple

a = ("python", "programme", "to","find","size","of","a","tuple")
print("Size of the tuple is", len(a))



#find maximum and minimum k elements in tuple

Tuple = (4, 9, 1, 7, 3, 6, 5, 2)
K = 2
sortedColl = sorted(list(Tuple))
vals = tuple(sortedColl[:K] + sortedColl[-K:])
print("Tuple : ", str(myTuple))
print("K maximum and minimum values : ", str(vals))