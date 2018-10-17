message = input('enter some number: ')
print(message)
#t1 = message > 18
t2 = int(message) > 18
#print(str(t1))
print(str(t2))

numGuests = input("What is the size of your Party?")
print(numGuests)

if int(numGuests) > 8:
    print('You will need to wait')
else:
    print('Follow me, we have a few tables overlooking the ocean?')