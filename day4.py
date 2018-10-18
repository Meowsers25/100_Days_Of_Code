from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

# classic tuple
user = ('bob', 'coder')
print(f'{user[0]} is a {user[1]}')

# namedtuple
User = namedtuple('User', 'name role')
user = User(name='Chris', role='Coding Genius')
print(user.name)
print(user.role)
# f strings are awesome
print(f'{user.name} is a true {user.role}.')

# use a namedtuple wherever you can! They are #easy to implement and make your code more #readable.

users = {'Chris': 'coder'}
print(users['Chris'])
# this causes an EnvironmentError
# print(users['Julian'])
print(users.get('Chris'))
# this gives us none
print(users.get('Julian'))

challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),('mike', 11), ('julian', 8), ('bob', 6)]

print(challenges_done)

# challenges = {}
# for name, challenge in challenges_done:
#   challanges[name].append(challenge)
# print(challenges)


words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
print(words[:5])
# using Counter......WOW
print(Counter(words).most_common(5))

