def name_check():
    name = 'oleksandr'
    x = input("Do you know my name? Let's check it! Say (enter) my name.\n")
    return True if x.lower() == name else False


print(name_check())

