class Computer: #1. defineeri klass

    def __init__(self): #2. loome konstruktori
        self.__selling_price = 700 #3. 4. defineeri ja väärtusta väljad
        self.public_price = 1000

    def sell(self): #5. tee midagi kasulikku
        print(f"Selling Price: {self.__selling_price}")
        print(f"Public Price: {self.public_price}")

    def __upcharge__(self):
        self.__selling_price += 100

    def set_selling_price(self, price):
        if price < 0:
            raise Exception("Sorry, you cannot sell negative price")
        self.__selling_price = price

if __name__ == '__main__':
    c = Computer()
    c.sell()

    # change the price
    c.__selling_price = 1000
    c.__upcharge__()
    c.public_price = -1000
    c.sell()

    # setting selling price using setter function
    c.set_selling_price(1000)
    c.sell()
