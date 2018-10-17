

#print(list.sort(self, cmp, key=lambda x : len x, reverse))

dinnerInvites = ['sonali', 'Aliya', 'Tiffiny']
salutation = 'ms.'

print("\n Dear " + salutation.upper() + " " + dinnerInvites[0].title() + " you have been invited to dinner")
print("\n Dear " + salutation.upper() + " " + dinnerInvites[1].title() + " you have been invited to dinner")
print("\n Dear " + salutation.upper() + " " + dinnerInvites[2].title() + " you have been invited to dinner")

declined = dinnerInvites[0]
print("\nA" + salutation.upper() + " " + declined.upper() + "wont be attending")

dinnerInvites[0] = 'Jane'

print(dinnerInvites)

dinnerInvites.append('Mr End')
dinnerInvites.insert(0,'Ms Begining')
lenght = len(dinnerInvites)
print(round(lenght/2,0))

dinnerInvites.insert(2,'Mr Middle')

unSortDinner = dinnerInvites

dinnerInvites.sort(reverse=True)
print(dinnerInvites)

print(sorted(unSortDinner, reverse=True))
print(unSortDinner)



dinnerInvites.pop(0)
print(dinnerInvites)

dinnerInvites.pop(3)
print(dinnerInvites)

dinnerInvites.pop(2)
print(dinnerInvites)

dinnerInvites.pop(1)
print(dinnerInvites)

del dinnerInvites[1]
print(dinnerInvites)

del dinnerInvites[0]
print(dinnerInvites)


