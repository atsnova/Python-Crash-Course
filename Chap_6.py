aliens = {1:1,2:2,3:'three',4:4,'six':'five'}

apples = [1,2,3,4,5,6]

print(aliens.__class__)
print(apples.__class__)

# for alien in aliens:
#     print(alien)
#     if alien < 5:
#         aliens[alien] = 99


for apple in apples:
    print(apple)
    if apple < 5:
        apples[apple] = 99


print(aliens[1])


names = {'jane':'C','peter':'python','matt':'C#','atish':'SQL'}

for name in names:
    print(name.title() + " " + names[name].title())

for k,v in names.items():
    print(k.title() + " : " + v.title())

for alien in aliens.values():
    print(alien)