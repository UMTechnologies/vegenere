def gamma_generator(message, key):
    key *= len(message) // len(key) + 1
    return key


def alphabet_generator():
    data = chr(65)
    for i in range(65, 65+26):
        print(chr(i), end=' ')


def encryption(message, key):
    while len(message) > len(key):
        key = gamma_generator(message, key)
        gamma = key
        text = ''
        for i, a in enumerate(message):
            num = (ord(a) + ord(gamma[i]))
            text = text + chr(num % 26 + 65)
        return text


def decryption(message, key):
    while len(message) > len(key):
        key = gamma_generator(message, key)
        gamma = key
        text = ''
        for i, a in enumerate(message):
            num = (ord(a) - ord(gamma[i]))
            text += chr(num % 26 + 65)
        return text


if __name__ == '__main__':
    print("Welcome to Vegenere encrypt / decrypt service. Please select what do you want: ")
    while True:
        print("---------------------------------")
        print("Type 1: For gamma generator")
        print("Type 2: For encryption")
        print("Type 3: For decryption")
        print("Type 4: Supported alphabet: ENG")
        print("---------------------------------")
        print(">>> To quit press control + C <<<")
        print("---------------------------------")
        cmd = int(input("Select command: "))

        if cmd == 4:
            print("Currently supported symbols: ")
            alphabet_generator()
        elif cmd == 3:
            message = input("Write your encrypted message: ")
            key = input("Type your key: ")
            print("Result: " + decryption(message, key))
        elif cmd == 1 or cmd == 2:
            message = input("Write your message: ")
            key = input("Type your key: ")
            if cmd == 1:
                print("Your gamma: " + gamma_generator(message, key))
            elif cmd == 2:
                print("Encrypted text: " + encryption(message, key))
        else:
            print("Wrong command - please try again :(")

        print("\n")
        print("\n")

