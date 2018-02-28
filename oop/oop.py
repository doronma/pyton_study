class Kettle(object):

    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

    def switch_off(self):
        self.on = False

kenwood = Kettle("Kenwood",8.99)
print(kenwood.make)
print(kenwood.price)
kenwood.price = 5.5
print(kenwood.price)

print("Models: {0.make} = {0.price}".format(kenwood))

print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

Kettle.switch_off(kenwood)
print(kenwood.on)

print("*"*80)
kenwood.power = 1.5
print("kenwood.power - {}".format(kenwood.power))

