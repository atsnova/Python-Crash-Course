class Resturant(object):
    """docstring for Resturant"""
    def __init__(self, resturant_name, cuisine_type):
        """give it a name and cusinie type :) """
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
    
    def describe_resturant(self):
        print("The name of the Resturant is " + str(self.resturant_name))
        print("\nWe serve " + self.cuisine_type + " cuisine")

    def open_resturant(self):
        print("We now open for business, closing time is 21h00")

Punitas = Resturant("HotShot","Spicy Indian")

#print(Punitas.cuisine_type.lower())
#print(Punitas.resturant_name)
#print("My resturant's name is " + resturant_name)

#print(Punitas.open_resturant())

Punitas.describe_resturant()
Punitas.open_resturant()