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

#Comment is a great part of coding

#Slicing through List
players = ["mike", "khalid", "tope", "olamide", "tayo","timo","marve","yinka","fola"]

print("The first three players are:")
print(players[:3])

print("\nThe second three players are:")
print(players[3:6])

print("\nThe third three players are:")
print(players[6:])

#Copying a list
pizzas = ["dominos", "ola", "lade","toun"]
friend_pizzas = pizzas[:]

pizzas.append("novar")
friend_pizzas.append("zealot")

print("My fav pizza are :")
for pizza in pizzas[0:]:
  print(pizza.title())

print("\nMy friend's fav pizza are :")
for friend in friend_pizzas[0:]:
 print(friend.title())



#Looping through a slice
for player in players[:2]: 
   print(player.title())

