prompt = "\nWhat is your car selection?" 
prompt += "\nEnter Q to quit:\n"

cardemand = ""
while cardemand != "Q":
    cardemand = input(prompt)
    if cardemand == "Q": 
        break
    print("Let me see if I can find you a " + cardemand.title())


active = "True"
while active:
    cardemand = input(prompt)
    if cardemand !='Q':
        active = False
    else: 
         print("Let me 2sd if I can find you a " + cardemand.title())

