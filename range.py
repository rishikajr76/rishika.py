def my_range(*args):
    if len(args) == 1:
        i = 0
        while(i < args[0]):
            yield i
            i += 1
    elif len(args) == 2:
        i = 0
        while(i < args[1]):
            yield i
            i += 1
    elif len(args) == 3:
        i = args[0]
        if args[0] < args[1] and args[0] < args[2]:
            while(i < args[0]):
                yield i
                i += 1


input_number = int(input('Enter a small number of your choice:'))
