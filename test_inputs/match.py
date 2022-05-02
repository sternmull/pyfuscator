def f1(x):
    y = 'initial y'
    a, b = 'initial a', 'initial b'
    match x:
        case 1:
            print('one')
        case a, b:
            print('a, b in case are', a, b)
        case y:
            print('y in case is', y)

    print('y after match is', y)
    print('a, b after match are', a, b)

f1(1)
f1(11)
f1(('alpha', 'beta'))
