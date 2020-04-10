def gen_pwd():
    from random import randrange
    components = {
        "color": ["blue", "red", "purple", "green", "yellow", "orange", "black", "white"],
        "number": 50,
        "noun": ["cat", "dog", "table", "chair", "monitor", "computer", "meal", "dessert", "chocolate", "hammer"],
        "char": [';', ':', '<', '>', '|', '?', '-', '!', '@', '.']
    }
    new_pass = ""
    for key in components:
        if key == "number":
            new_pass += str(randrange(components[key] + 1))
        else:
            loop_num = 1
            if key == "char":
                loop_num = 4
            for _ in range(loop_num):
                new_pass += components[key][randrange(len(components[key]))]
    return new_pass

def main():
    user_ans = input("Do you want to generate a new password? (y/n) ").lower()
    while user_ans not in ('y', 'n'):
        print("\nThat is not a valid option.\n")
        user_ans = input("Do you want to generate a new password? (y/n) ").lower()
    if user_ans == 'y':
        print("\nNew password: {}\n".format(gen_pwd()))
        main()
    else:
        print("\nThank you for using the password generator!\n")

print ("This program will generate a secure password for you to use.")
main()