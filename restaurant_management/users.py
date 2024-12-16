from abc import ABC
from menu import Menu
from order import Order

class User(ABC):
	def __init__(self, name, email, phone_no, address):
		self.name = name
		self.email = email
		self.phone_no = phone_no
		self.address = address


class Customer(User):
	def __init__(self, name, email, phone_no, address):
		super().__init__(name, email, phone_no, address)
		self.cart = Order()

	def view_menu(self, restaurant):
		restaurant.menu.show_menu()


	def add_to_cart(self, restaurant, item_name, quantity):
		item = restaurant.menu.find_item(item_name)

		if item:
			if quantity > item.quantity:
				print("item quantity exceeded !!")
			else:
				item.quantity = quantity
				self.cart.add_item(item)
				print("item added ...")
		else:
			print("item not found")


	def view_cart(self):
		print("********* Menu **********")
		print("Name\tPrice\tQuantity")
		for item, quantity in self.cart.items.items():
			print(f"{item.name}\t{item.price}\t{quantity}")


	def pay_bill(self):
		print(f"total {self.cart.total_price()} tk paid successfully")





class Employee(User):
	def __init__(self, name, email, phone_no, address, age, designation, salary):
		super().__init__(name, email, phone_no, address)
		self.age = age
		self.designation = designation
		self.salary = salary



class Admin(User):
	def __init__(self, name, email, phone_no, address):
		super().__init__(name, email, phone_no, address)


	def add_employee(self, restaurant, employee):
		restaurant.add_employee(employee)


	def view_employee(self, restaurant):
		restaurant.view_employee()


	def add_new_item(self, restaurant, item):
		restaurant.menu.add_menu_item(item)


	def view_menu(self, restaurant):
		restaurant.menu.show_menu()


	def remove_item(self, restaurant, item_name):
		restaurant.menu.remove_item(item_name)