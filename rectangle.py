tuple_list = []
for w in range(2,10):
  for h in range(3,10):
    tuple_list.append((w,h))

sorted_list = sorted(tuple_list, key=lambda tup: (tup[0] - 1) * (tup[1] - 1))

print(sorted_list)