alists = ['item one', 'i wont cry', 'there is an',
    'ordinary', 'love', 'i will', 'survive']

print("the first three items in this list are:")
for val in alists[0:3]:
    print(val)

print("the three items in the middle of the list are:")
for val in alists[2:5]:
    print(val)

print("the three items in the end of the list are:")
for val in alists[4:]:
    print(val)

blists = alists[:]
alists.append('singer')

print(blists)


foods = ('apple', 'carrots', '12312', 'gem', 'watermelon')


for counter in foods:
    print(counter)

print(foods[0])
