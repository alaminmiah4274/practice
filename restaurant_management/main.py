
from food_item import FoodItem 
from order import Order
from menu import Menu
from restaurant import Restaurant
from customer_interface import customer_menu
from admin_interface import admin_menu


mayer_hotel = Restaurant("Mayer Dua Hotel")


while True:
	print("Welcome !!")
	print("1. Customer")
	print("2. Admin")
	print("3. Exit")

	choice = int(input("Enter your choice : "))

	if choice == 1:
		customer_menu(mayer_hotel)
	elif choice == 2:
		admin_menu(mayer_hotel)
	elif choice == 3:
		break
	else:
		print("invalid input")