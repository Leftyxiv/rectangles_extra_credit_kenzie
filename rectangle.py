import random 

tuple_list = []
wide = random.randint(2,9)
height = random.randint(wide + 1, 10)
for w in range(2,wide):
  for h in range(3,height):
    tuple_list.append((w,h))

sorted_list = sorted(tuple_list, key=lambda tup: (tup[0] - 1) * (tup[1] - 1))

print(sorted_list)