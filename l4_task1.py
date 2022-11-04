def str_manipulation():
    string = input('Enter text\n')
    if len(string) < 2:
        return ''
    else:
        return string[:2] + string[-2:]


print(str_manipulation())
