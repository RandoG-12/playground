# create an empty set
s = set()
print(f"\nempty set: {s}")

# add elements to set
s.add(1)
s.add(4)
s.add(3)
s.add(2)
print(f"\nset after add 1 4 3 2: {s}")

s.add(3)
print(f"\nset after duplicate add 3: {s}")

s.remove(2)
print(f"\nset after remove 2: {s}")

print(f"\nthere are {len(s)} elements in set s.")

print()
