class IceCream(object):
    def __init__(self, flavor, popularity):
        self.flavor = flavor
        self.popularity = popularity

    def iceCreamDetails(self):
        return print("The ice cream is " + strawberry.flavor)

    def popularityDetails(self):
        return print("The ice cream's popularity is " + strawberry.popularity)


iceCreamInput = input("Which ice cream do you want to know the details of? Vanilla or Strawberry?")
strawberry = IceCream("Strawberry", "100")
vanilla = IceCream("Vanilla", "150")

if iceCreamInput == "strawberry":
    print(strawberry.iceCreamDetails())
    print(strawberry.popularityDetails())

elif iceCreamInput == "vanilla":
    print(vanilla.iceCreamDetails())
    print(vanilla.popularityDetails())

else:
    print("That ice cream is not found in our system. Please choose one of the options given")

