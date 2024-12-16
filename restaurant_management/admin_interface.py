from users import Admin, Employee
from food_item import FoodItem

def admin_menu(restaurant):
	name = input("Enter your name : ")
	email = input("Enter your email : ")
	phone_no = input("Enter your phone no : ")
	address = input("Enter your address : ")

	admin = Admin(name, email, phone_no, address)

	while True:
		print(f"Welcome {admin.name} !!")
		print("1. Add new item : ")
		print("2. Add new employee : ")
		print("3. View employee : ")
		print("4. View item : ")
		print("5. Delete item : ")
		print("6. Exit : ")

		choice = int(input("Enter your choice : "))

		if choice == 1:
			item_name = input("Enter item name : ")
			item_price = int(input("Enter item price : "))
			item_quantity = int(input("Enter item quantity : "))

			item = FoodItem(item_name, item_price, item_quantity)

			admin.add_new_item(restaurant, item)
		elif choice == 2:
			emp_name = input("Enter your empoyee name : ")
			emp_email = input("Enter your empoyee email : ")
			emp_phone_no = input("Enter your empoyee phone no : ")
			emp_address = input("Enter your empoyee address : ")
			emp_age = input("Enter your empoyee age : ")
			emp_designation = input("Enter your empoyee designation : ")
			emp_salary = int(input("Enter your empoyee salary : "))

			employee = Employee(emp_name, emp_email, emp_phone_no, emp_address, emp_age, emp_designation, emp_salary)

			admin.add_employee(restaurant, employee)
		elif choice == 3:
			admin.view_employee(restaurant)
		elif choice == 4:
			admin.view_menu(restaurant)
		elif choice == 5:
			item_name = input("Enter item name : ")
			admin.remove_item(restaurant, item_name)
		elif choice == 6:
			break
		else:
			print("invalid input")