pizza =['mushroom', 'olive', 'tomatoes', 'herbs']

if 'anchovies' not in pizza:
    print('Yummy mushrooms')
else:
    print('lets get sushi rather')


toppings = []

for x in pizza:
    if x in toppings:
        print('Baking your pizza')
    elif x not in toppings:
        print("Adding " + x + " to your pizza")
    else:
        print('Baking your pizza')

toppings = ['mushroom']

for x in pizza:
    if x not in toppings:
        print("Adding " + x + " to your pizza")
    else:
        print('Baking your pizza')


users = ('admin', 'eric' , 'aliya' , 'candice' , 'terry')

for user in users:
    if user == 'admin':
        print("Hello Admin, what to see a status report.")
    else:
        print("Welcome back " + user.title())



for i in range(1,10):
    if i == 1:
        print(str(i) + "st")
    elif i == 2:
        print(str(i) + "nd")
    elif i ==3 :
        print(str(i) + "rd")
    else:
        print(str(i) + "th")
