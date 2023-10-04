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

