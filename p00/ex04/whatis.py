import sys


def whatis():
    """
    Fonction affiche si un nombre est pair ou impair
    """
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided"
              if len(sys.argv) > 2 else "AssertionError: no argument provided")
        return

    arg = sys.argv[1]

    try:
        number = int(arg)
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
