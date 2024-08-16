# def all_thing_is_obj(object: any) -> int:
# 	if isinstance(object, list):
# 		print(f"List : {type(object)}")
# 	elif isinstance(object, tuple):
# 		print(f"Tuple : {type(object)}")
# 	elif isinstance(object, set):
# 		print(f"Set : {type(object)}")
# 	elif isinstance(object, dict):
# 		print(f"Dict : {type(object)}")
# 	elif isinstance(object, str):
# 		print(f"{object} is in the kitchen  : {type(object)}")
# 	return 42

def all_thing_is_obj(obj: any) -> int:
	type_map = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
		str: "String"
	}

	if type(obj) in type_map:
		if type(obj) == str:
			print(f"{obj} is in the kitchen  : {type(obj)}")
		else:
			print(f"{type_map[type(obj)]} : {type(obj)}")

	return 42
