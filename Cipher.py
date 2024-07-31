import argparse
import shlex
import sys

def negasht(code):
    dict_str = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25
    }

    dict_int = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",
        14: "O",
        15: "P",
        16: "Q",
        17: "R",
        18: "S",
        19: "T",
        20: "U",
        21: "V",
        22: "W",
        23: "X",
        24: "Y",
        25: "Z"
    }

    if isinstance(code, str):
        return dict_str.get(code.upper(), None)
    if isinstance(code, int):
        return dict_int.get(code, None)
    return None


def Alg_Additive_Cipher(text, key):
    word_list = []

    for char in text:
        if char.isalpha():
            x = negasht(char.upper())
            if x is not None:
                code = (x + key) % 26
                word = negasht(code)
                word_list.append(word)
        elif char == ' ':
            word_list.append(' ')

    return ''.join(word_list)


def Alg_Multiplicative_Cipher(text, key):
    word_list = []

    for char in text:
        if char.isalpha():
            x = negasht(char.upper())
            if x is not None:
                code = (x * key) % 26
                word = negasht(code)
                word_list.append(word)
        elif char == ' ':
            word_list.append(' ')

    return ''.join(word_list)


def Alg_Affine_Cipher(text, a, b):
    word_list = []

    for char in text:
        if char.isalpha():
            x = negasht(char.upper())
            if x is not None:
                code = (x * a + b) % 26
                word = negasht(code)
                word_list.append(word)
        elif char == ' ':
            word_list.append(' ')

    return ''.join(word_list)


def Alg_Mapping_Cipher(text, mapping):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_dict = {alphabet[i]: mapping[i].upper()
                   for i in range(len(alphabet))}

    encrypted_text = ''.join(cipher_dict.get(
        char.lower(), char) for char in text)

    return encrypted_text.upper()


def process_input(command):
    parser = argparse.ArgumentParser(
        description='Encrypt text using various cipher algorithms.')
    parser.add_argument('cipher_type', choices=[
                        "additive-cipher", "multiplicative-cipher", "affine-cipher", "mapping-cipher"])
    parser.add_argument('-text', required=True)
    parser.add_argument('-key', type=int, default=None)
    parser.add_argument('-a', type=int, default=None)
    parser.add_argument('-b', type=int, default=None)
    parser.add_argument('-mapping', type=str, default=None)

    args = parser.parse_args(shlex.split(command))

    text = args.text.strip()

    if args.cipher_type == "additive-cipher":
        key = args.key
        return Alg_Additive_Cipher(text, key)
    elif args.cipher_type == "multiplicative-cipher":
        key = args.key
        return Alg_Multiplicative_Cipher(text, key)
    elif args.cipher_type == "affine-cipher":
        a = args.a
        b = args.b
        return Alg_Affine_Cipher(text, a, b)
    elif args.cipher_type == "mapping-cipher":
        mapping = args.mapping.strip().strip('"')
        return Alg_Mapping_Cipher(text, mapping)


def main():
    print("\nWelcome to the Cipher Algorithms program!")
    print("This program supports the following ciphers:")
    print("1. Additive Cipher")
    print("2. Multiplicative Cipher")
    print("3. Affine Cipher")
    print("4. Mapping Cipher")
    print("\nUsage examples:")
    print('* additive-cipher -text "HELP me" -key 1')
    print('* multiplicative-cipher -text "danger" -key 3')
    print('* affine-cipher -text "example" -a 5 -b 8')
    print('* mapping-cipher -text "hello" -mapping "phqgiumeaylnofdxjkrcvstzwb"')
    print("\nPlease enter the number of commands followed by the ")

    n = int(input().strip())
    results = []

    for i in range(n):
        command = input(f"{i+1} : ").strip()
        try:
            result = process_input(command)
            results.append(result)
        except Exception as e:
            results.append(str(e))

    print("\n------Result------")
    for result in range(len(results)):
        print(f"[{result+1}] : ", results[result])


if __name__ == "__main__":
    main()
    if len(sys.argv) != 2:
        print("Usage: python cipher.py <text>")
        sys.exit(1)
    text = sys.argv[1]
    print(process_input(text))