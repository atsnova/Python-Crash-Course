response = {}

#Populate it

value = True
while value != False:
    name = input('enter name into  responses')
    if name.lower() == 'no':
        value = False
        exit()
    poll = input('enter value of poll')

    response[name] = poll
    value = input('enter another name?')
    if value == 'no':
        value = False

print(response)