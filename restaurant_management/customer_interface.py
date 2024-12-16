from users import Customer


def customer_menu(restaurant):
	name = input("Enter your name : ")
	email = input("Enter your email : ")
	phone_no = input("Enter your phone no : ")
	address = input("Enter your address : ")

	customer = Customer(name, email, phone_no, address)

	while True:
		print(f"Welcome {customer.name}")
		print("1. View menu : ")
		print("2. Add item to cart : ")
		print("3. View cart : ")
		print("4. Pay Bill : ")
		print("5. Exit : ")

		choice = int(input("Enter your choice : "))

		if choice == 1:
			customer.view_menu(restaurant)
		elif choice == 2:
			item_name = input("Enter item name : ")
			item_quantity = int(input("Enter item quantity : "))
			customer.add_to_cart(restaurant, item_name, item_quantity)
		elif choice == 3:
			customer.view_cart()
		elif choice == 4:
			customer.pay_bill()
		elif choice == 5:
			break
		else:
			print("invalid input")