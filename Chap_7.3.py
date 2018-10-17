#def pizzaTopping():
message = "What type of Pizza topping do you want?"
message += "\n Enter 'quit' to stop entering toppings"   

toppings = []
topping =''

while topping != "quit":
    topping = input(message)
    toppings.append(topping)


#return toppings
#print(pizzaTopping())
print('We will add the following toppings: ' + str(toppings))