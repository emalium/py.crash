#pop from any position
network = ["airtel", "mtn", "glo", "9mobile"]
print(network)
popped_network = network.pop()
print(popped_network)
best_network = network.pop(-1)
print(f"{best_network.title()} is the poorest network in Nigeria")

family = ["dad", "mum","pete","kudus","subom"]
comot = "pete"
family.remove(comot)
print(f"\n{comot.title()} not part of the family")

