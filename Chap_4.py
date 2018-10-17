names = ['sonali', 'Aliya', 'Tiffiny', 'Cards', 'pillow' , 'monitor', 'johnny']

for name in names:
    print(name + "\nGuest at the party " + name.title())

numbers =  list(range(25,0,-5))
for number in numbers:
    print(number)

for value in range(0,30,3):
    print(value)


squares = []
for value in range(0,11):
    square =  value**2
    squares.append(square)
    print(squares)
    squares.pop(-1)
    print(squares)

for value in range(1,21):
    print(value)

million = list(range(1,1000001))
print(sum(million))
print(min(million))
print(max(million))


odds = list(range(1,20,2))
print(odds)

for odd in odds:
    print(odd)

cubes = list(range(1,11))
print(cubes)

cubes = []
for value in range(1,11):
    cube=value**3
    cubes.append(cube)
    print(cubese)
print(cubes)