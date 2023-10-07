party = ["adewunmi","emmanuel","olajide"]
print(party[0], "are hereby invited to my party")
print(party[1], "are hereby invited to my party")
print(party[2], "are hereby invited to my party")

unavailable = party.pop(0)
print(f"{unavailable.title()}, won't be around" )
party[1] = "imole"
print(party)

party = ["adewunmi","emmanuel","olajide"]
print("Found a bigger event centre,", party)
party.insert(0,"samuel")
party.insert(1,"esther")
party.insert(2,"elijah")
print(party)

print("Sorry, only two people can be invited")
out = party.pop(-1)
print(f"Sorry you are no longer inivited {out.title()}")
out = party.pop(-1)
print(f"Sorry you are no longer invited {out.title()}")
out = party.pop(-1)
print(f"Sorry you are no longer inivited {out.title()}")
out = party.pop(-1)
print(f"Sorry you are no longer inivited {out.title()}")

print(party[-1], "you are still invited ma")
print(party[-2], "you are still invited sir")

del party[-1]
print (party)
del party [-1]
print(party)

#Still working with List

locations =["dubai", "california", "shockholm", "maldives"]
print(locations)

sorted_locations = sorted(locations)
print(sorted_locations)

print(locations)

print(sorted(locations, reverse=True))

print(locations)

locations.reverse
print(locations)

locations.sort()
print(locations)

locations_len = len(locations)
print(locations_len)

#More on List

pizzas = ["dominos", "ola's", "lade","toun"]
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza\n")
print("I really love eating Pizza")    

animals = ["goat","cock", "cat","dolphin"]
for animal in animals :
    print(f"\nA {animal.title()} would make a great pet")
    print(f"All {animal.title()} are pets\n")
print("Any of this animal will make a great pet")    

# how you might make a list of the first 10 number
squares = []
for value in range(1,11):
   squares.append (value**2)
print(squares) 
#There is also another method in solving this quetion

#More on List
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
    

