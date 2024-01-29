class Shirt:
    def __init__(self, shirt_color, shirt_style, shirt_size, shirt_price):
        self.color = shirt_color
        self.style = shirt_style
        self.size = shirt_size
        self.price = shirt_price
    
    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)
    
new_shirt = Shirt('red', 'long sleeve', 'm', 50)
# new_shirt.change_price(50)
print(new_shirt.price)
print(new_shirt.size)
print(new_shirt.discount(.2))

