def NULL_not_found(object: any) -> int:
	# Détection et impression pour les types spécifiques
	if object is None:
		print(f"Nothing: {object} {type(object)}")
	elif isinstance(object, float) and (object != object):  # Vérifie NaN
		print(f"Cheese: {object} {type(object)}")
	elif isinstance(object, str) and object == '':
		print(f"Empty: <class 'str'>")
	elif isinstance(object, bool) and not object:
		print(f"Fake: {object} {type(object)}")
	elif isinstance(object, int) and object == 0:
		print(f"Zero: {object} {type(object)}")
	else:
		print("Type not Found")
		return 1
	return 0

