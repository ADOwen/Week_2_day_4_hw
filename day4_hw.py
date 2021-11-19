

class ShoppingCart():

    def __init__(self, dict={}):
        self.dict = dict

    def addCart(self):
        item = input(
            "\nPlease enter the item you would like to add to shopping cart: ")
        quantity = input("\nHow many would you like? ")
        self.dict[item] = quantity
        print(self.dict)

    def showCart(self):

        if self.dict:
            for self.item, self.quantity in self.dict.items():
                print(f"\n{self.quantity} : {self.item.title()}")
        else:
            print('\nYour cart is empty')

    def clearCart(self):
        if self.dict:
            self.dict.clear()
            print("\nYour cart has been cleared")
        else:
            print("\nYour cart is empty")

    def quitCart(self):
        if self.dict:
            print("\nHere's your final order, thanks for shopping with us")
            print('====================================================')
            for item, quantity in self.dict.items():
                print(f"\n{quantity} : {item.title()}")
                self.running = False
        else:
            self.running = False

    def run(self):
        self.running = True
        while self.running:

            question = input(
                "\nWould you like to [S]how cart, [A]dd item [C]lear or [Q]uit? ")

            if question.lower() == 'a':
                self.addCart()

            if question.lower() == 'c':
                self.clearCart()

            if question.lower() == 's':
                self.showCart()

            if question.lower() == 'q':
                self.quitCart()


my_bag = ShoppingCart()

my_bag.run()

# exercise 2
