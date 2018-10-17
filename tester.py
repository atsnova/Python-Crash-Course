def getTranslatedMessage(message):     


    for symbol in message:
        print(symbol)
        if symbol.isalpha():
            num =   symbol)
            num += 1
            print(num)

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated



print(getTranslatedMessage("A"))