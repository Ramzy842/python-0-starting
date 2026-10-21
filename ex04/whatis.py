import sys

try:
    if len(sys.argv) < 2:
        sys.exit(0)

    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    try:
        arg = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if arg % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as error:
    print(f"AssertionError: {error}", file=sys.stderr)
    sys.exit(1)