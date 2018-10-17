#def pizzaTopping():
message1 = "What Pizza do you want?"
message = "What type of Pizza topping do you want?"
message += "\n Enter 'quit' to stop entering toppings"   

pizzas = {}


while True:
    pizza = input(message1)
    topping = input(message)

    if topping == "quit":
        break
    else:
        pizzas[pizza] = topping
        #toppings.append(topping)


#return toppings
#print(pizzaTopping())
#print('We will add the following toppings: ' + str(toppings))
print(pizzas)