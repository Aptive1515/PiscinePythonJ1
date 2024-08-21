import sys
from ft_filter import ft_filter


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("AssertionError: more than two argument is provided"
              if len(sys.argv) > 3 else "AssertionError: no argument provided")
        exit()

    arg = sys.argv[2]

    try:
        number = int(arg)
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit()

    ft_filter(sys.argv[1], number)
