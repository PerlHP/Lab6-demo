# this is a file I created

def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def main():
    decoded_val = 0
    encoded_pass = 0
    pass_to_encode = ""

    while True:
        print_menu()
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            pass_to_encode = input("Please enter your password to encode: ")
            encoded_pass = encode(int(pass_to_encode))
            print("Your password has been encoded and stored!")
        elif user_option == 2:
            # decode 
            print("This is a decode")
        elif user_option == 3:
            exit()

def encode(initial_pw):
    return initial_pw + 33333333
    
if __name__ == '__main__':
    main()