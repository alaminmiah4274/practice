class Item:
	def __init__(self, item_name, price, quantity):
		self.item_name = item_name
		self.price = price
		self.quantity = quantity


class Order:
	def __init__(self):
		self.items = {}


	def add_item(self, item):
		if item in self.items:
			self.items[item] += item.quantity
		else:
			self.items[item] = item.quantity


	def show_item(self):
		print("Name\tPrice\tQuantity")
		for key, value in self.items():
			print(f"{item.item_name}\t{item.price}\t{item.quantity}")



food = Item("Banana", 10, 5)
food2 = Item("Apple", 25, 3)
food3 = Item("Orange", 20, 2)

my_order = Order()
my_order.add_item(food)
my_order.add_item(food2)
my_order.add_item(food3)

my_order.show_item()