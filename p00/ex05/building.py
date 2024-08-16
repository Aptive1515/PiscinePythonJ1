import sys
import string

def count_printable(s: str) -> int:
	"""
	Compte le nombre de lettres dans la chaîne donnée.

	:param s: Chaîne de caractères à analyser
	:return: Nombre de lettres dans la chaîne
	"""
	return sum(c.isprintable() for c in s)

def count_uppercase(s: str) -> int:
	"""
	Compte le nombre de lettres majuscules dans la chaîne donnée.

	:param s: Chaîne de caractères à analyser
	:return: Nombre de lettres majuscules dans la chaîne
	"""
	return sum(c.isupper() for c in s)

def count_lowercase(s: str) -> int:
	"""
	Compte le nombre de lettres majuscules dans la chaîne donnée.

	:param s: Chaîne de caractères à analyser
	:return: Nombre de lettres majuscules dans la chaîne
	"""
	return sum(c.islower() for c in s)

def count_spaces(s: str) -> int:
	"""
	Compte le nombre de lettres majuscules dans la chaîne donnée.

	:param s: Chaîne de caractères à analyser
	:return: Nombre de lettres majuscules dans la chaîne
	"""
	return sum(c == " " for c in s)

def count_digit(s: str) -> int:
	"""
	Compte le nombre de lettres majuscules dans la chaîne donnée.

	:param s: Chaîne de caractères à analyser
	:return: Nombre de lettres majuscules dans la chaîne
	"""
	return sum(c.isdigit() for c in s)

def count_punctuation(s: str) -> int:
	"""
	Compte le nombre de signes de ponctuation dans la chaîne donnée.

	:param s: Chaîne de caractères à analyser
	:return: Nombre de signes de ponctuation dans la chaîne
	"""
	return sum(c in string.punctuation for c in s)


def count_all(string:str):
	print(f"The text contains {count_printable(string)} characters:")
	print(f"{count_uppercase(string)} upper letters")
	print(f"{count_lowercase(string)} lower letters")
	print(f"{count_punctuation(string)} punctuation marks")
	print(f"{count_spaces(string)} spaces")
	print(f"{count_digit(string)} digits")


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("AssertionError: more than one argument is provided" if len(sys.argv) > 2 else "AssertionError: no argument provided")
		exit()
	count_all(sys.argv[1])
