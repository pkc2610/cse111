def get_things_from_file(file_name):
    things = []
    with open(file_name, "r") as file:
        for i in file.readlines():
            things.append(i.strip())
        print(things)
    return things


def add_thing(listy_boi):
    extra_thing = input("What would you like to add? ")
    listy_boi.append(extra_thing)
    print(listy_boi)
    return listy_boi

def remove_thing(listy_boi):
    one_less_thing = input("What would you like to remove? ")
    listy_boi.remove(one_less_thing)
    print(listy_boi)
    return listy_boi

def sort_list(listy_boi):
    listy_boi.sort()
    print(listy_boi)
    return listy_boi

def save_list(listy_boi, file_name):
    with open(file_name, "w") as file:
        for i in listy_boi:
            file.write(i)
            file.write("\n")

def main():
    echo_baby = get_things_from_file("to_dos.txt")

    ooptions = input("if you want to add something, hit 'a', if you want to remove something, hit 'r', if you want to sort, hit 's', and if you want to quit hit 'x'")

    while ooptions != 'x':
        if ooptions == 'a':
            echo_baby = add_thing(echo_baby)
        elif ooptions == 'r':
            echo_baby = remove_thing(echo_baby)
        elif ooptions == 's':
            sort_list(echo_baby)
        ooptions = input("is there anything else you want to do? ")

    print("Best of luck with your future endeavors!")
    
    save_list(echo_baby, "to_dos.txt")

main()