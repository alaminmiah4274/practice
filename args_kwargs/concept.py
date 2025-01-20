nums = [10, 78, 15, 20, 50]

person = {
	"name": "miah",
	"address": "uttara",
	"subejct": "CSE"
}

def value_print(*args, **kwargs):
	print(args, kwargs)


# value_print(nums, person)  # ([10, 78, 15, 20, 50], {'name': 'miah', 'address': 'uttara', 'subejct': 'CSE'}) {}


value_print(*nums, **person) # (10, 78, 15, 20, 50) {'name': 'miah', 'address': 'uttara', 'subejct': 'CSE'}