#def pizzaTopping():
message1 = "What sandwich do you want?"
message = "What type of Pizza topping do you want?"
message += "\n Enter 'quit' to stop entering toppings"   

sandwichs = []


while True:
    sandwich = input(message1)
    

    if sandwich == "quit":
        break
    else:
        #pizzas[pizza] = topping
        sandwichs.append(sandwich)


#return toppings
#print(pizzaTopping())
#print('We will add the following toppings: ' + str(toppings))
for sandwich in sandwichs:
    print('list of sandwiches to make are : ' + sandwich)

sandwichsc = sandwichs
for completed in sandwichsc:
    print('done making : ' + completed)
  