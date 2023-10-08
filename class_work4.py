#Working with List
for value in range(1,21):
    print(value)

"""million = list(range(1,1000000))
print(million)"""

a_million = list(range(1,1_000_000))
print(max(a_million))
print(min(a_million))
print(sum(a_million))

"""for value in range (1,20,2):
    print(value)"""

odd_number = range(1,20,2)
for odd in odd_number:
 print(odd)

'''for value in range (3,30,3):
   print(value)'''

threes = list(range(3,30,3))
for three in threes:
 print(f"\t{three}") 
 
cubes = []
for value in range(1,11):
   cubes.append(value**3)
print(cubes)   

first_10 = list(range(1,10,3))
print(first_10)
    #Slicing
r = [20,40,60,80]
r[1:4] = []
print(r)