import sys

def get_chars_count(txt: str):
    upp = 0
    low = 0
    pun = 0
    space = 0
    dig = 0
    for char in txt:
        if char.isupper():
            upp += 1
        elif char.islower():
            low += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            dig += 1
        elif is_punc(char):
            pun += 1
    return {
        "uppercase": upp,
        "lowercase": low,
        "punctuation": pun,
        "space": space,
        "digit": dig
    }

def is_punc(c):
    pun_set = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return c in pun_set

def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) < 2:
            txt = input("What is the text to count?\n") + "\n"
        else:
            txt = sys.argv[1]
        count = get_chars_count(txt)
        print(f"The text contains {len(txt)} characters:")
        print(f"{count['uppercase']} upper letters")
        print(f"{count['lowercase']} lower letters")
        print(f"{count['punctuation']} punctuation marks")
        print(f"{count['space']} spaces")
        print(f"{count['digit']} digits")
    except AssertionError as error:
        print(f"AssertionError: {error}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()