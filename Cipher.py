import numpy as np

def stringToNumeric(str):
    """ take a string and convert it to numeric value
        returns an array of values                      """

    num = []
    for letter in str.lower():
        num.append(ord(letter))
    return num

def numerictoString(listToConvert):
    """ take a string and convert it to numeric value
        returns an array of values                      """

    encryptedString = ''
    for values in listToConvert:
        encryptedString += chr(values)
    return encryptedString

def encodeDecode(message,key = 0 ):
    """ take an array of numbers and shift the values """
    lenghtMessage = len(message)
    encoder = [key]*lenghtMessage
    print(encoder)
    encodedMessage = np.add(message,encoder)
    print(encodedMessage)
    return encodedMessage.tolist()


str = 'Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.'
    # code goes here 
    #return str
charac = str
count = len(charac)
print(count)
print(charac[::-1])

cipher = {}
for letter in str:
    num = ord(letter)

    cipher[letter] = num

    # cipher.append(letter) 
   # cipher.value(letter).append(num)
#    print(num)
print(cipher)
# keep this function call here  

#print(stringToNumeric(str))
message = stringToNumeric(str)

#print(encodeDecode(message,1))
encrypted = encodeDecode(message,-9)
print(numerictoString(encrypted))











  