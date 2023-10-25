# this is a file I created

# sets up the menu
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


def main():
    # sets up variables
    decoded_val = 0
    encoded_pass = 0
    pass_to_encode = ""
    decoded_pass = 0

    # loops until user exits (option 3)
    while True:
        print_menu()
        # asks for user input
        user_option = int(input("Please enter an option: "))
        # encodes the password
        if user_option == 1:
            pass_to_encode = input("Please enter your password to encode: ")
            encoded_pass = encode(int(pass_to_encode))
            print("Your password has been encoded and stored!")
        # decodes the password
        elif user_option == 2:
            decoded_pass = decode(int(encoded_pass))
            print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}.')
        # exits the loop
        elif user_option == 3:
            exit()

# password encoder
def encode(initial_pw):
    return initial_pw + 33333333

# password decoder
def decode(encode_pass):
    return encode_pass - 33333333

if __name__ == '__main__':
    main()