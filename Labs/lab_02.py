import copy

l = [i for i in range(14)]
print(l)

print(l[:3])
print(l[::-3])

k = [1,2,3, '3', (4,7), [2,3,4]]

c = k[:]
c[1] = [7,8,9]

print(c,k)
print(id(c),id(k))

c[-1][1] = '7,8,9'
print(c,k)


c = k.copy()
c[1] = '7,8,9'
print(c,k)
print(id(c),id(k))

c = copy.deepcopy(k)
c[1] = '7,8,9'
print(c,k)
print(id(c),id(k))


l.insert(-23,4)
l.insert(23,4)

l[1:4] = [4,7,8,9,10]
print(l)


m = [[]]*10
m[3].append(1)
print (m)


m[3].append([1,2,3])
print(m)

m[3].extend([1,2,3])
print(m)


k = [2,2,4,4]


for i in k:
  if i%2:
    break
else:
  print('kiedy?')

k = [(87,86), (123,46), (13,43), (15,462), (485,123)]

c = k[:]
l = c.sort(reverse = True)
print(c)

c.reverse()
print(c)

l = [i for i in range(14)]

l[4] = 2

def foo_for(x,l):
  n = l.count(x)

  for i in range(n):
    l.remove(x)
  return l

def foo(x,l):
  while x in l:
      l.remove(x)
  return l
  
print(foo(2,l))

print(foo_for(3,l))

l = [i for i in range(14)]


def coDrugi(l):
  for i in range(1, len(l), 2):
    print(l[i])


coDrugi(l)


print(l[1::2])

l = [i for i in range(14)]

for i in range(len(l)-1, -1, -2):
  print(l[i])

# Zad 6
print(l[len(l)::-2])

l= [3,2,46,4,4]

# Zad 7
print([(index, val) for index, val in enumerate(l)])
k = [(index, val) for index, val in enumerate(l)]
# Zad 8
print(sorted(k, key=lambda x: x[1]))
# Zad 9
