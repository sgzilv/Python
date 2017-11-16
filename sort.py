print(sorted([1, 0, 5, -1, -3]))

print(sorted([1, 0, 5, -1, -3], key = abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
    

L2 = sorted(L, key=by_name)
print(L2)

#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    return t[1]

L3 = sorted(L, key = by_score, reverse = True)

print(L3)


