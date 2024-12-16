# declaration of nested dictionary ------> 

books = {
	"Ultra Learing": {"author": "scot h young", "total_page": 280},
	"atomic habits": {"author": "james clear", "total_page": 283},
	"thinking: fast and slowly": {"author": "nobel lauriate", "total_page": 345},
	"pragmatic programmer": {"author": "david hanson", "total_page": 487}
}


# iteration on nested dictionary ----->

# for name, details in books.items():
# 	print(name)
# 	for key, value in details.items():
# 		print(f"{key}: {value}")
# 	print()

item = {"name": "Ultra Learing", "author": "scot h young", "total_page": 280}


if item in books:
	print("yes")
else:
	print("no")

