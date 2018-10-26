numlist = [1, 2, 3, 4, 5]
print(numlist)
numlist.reverse()
print(numlist)
numlist.sort()  # sorts in ascending
print(numlist)

for num in numlist:
    print(num)  # they used str(num)

mystring = 'chris'
print(list(mystring))
print(mystring)
l = list(mystring)
print(l)
l.pop()
print(l)
l.append('t')
print(l)
l.insert(0, 't')
print(l)
del l[0]
print(l)

#  tuples are immutable. They can be talked to, but can't be manipulated

t = tuple(mystring)
print(t[0])
#  t.pop() throws error
print(t)  # when tuple prints out it will be in paren ()

# dictionaries
pets = {'Luna': 'dog', 'Beatrice': 'dog', 'Sully': 'cat'}
print(pets)

people = {}
people['Katie'] = 35  # syntax to add to dict [key] = value
print(people)
people['Chris'] = 46
print(people)

print(pets.keys())
for x in pets.keys():
    print(x)

for keys, values in people.items():
    print(f'{keys} is {values} years of age.')