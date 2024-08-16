import sys
import string

def printMorse(s : string) -> int:

	morse_code_dict = {
		'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
		'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
		'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
		'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
		'Y': '-.--', 'Z': '--..',
		'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
		'5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
		'.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
		'/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
		';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
		'"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'}
	morse_text = ''
	for char in s.upper():
		if char in morse_code_dict:
			morse_text += morse_code_dict[char] + ' '
	print (f"{morse_text}")
	return 1

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("AssertionError: more than two argument is provided" if len(sys.argv) > 2 else "AssertionError: no argument provided")
		exit()
	s = sys.argv[1]

	for word in s :
		if word.isalpha() != 1:
			print("AssertionError: the arguments are bad")
	printMorse(s)
