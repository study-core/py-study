import sys

def check_python():
    info = sys.version_info
    if info[0] == 2 and not info[1] >= 6:
        print('Python 2.6+ required')
        sys.exit(1)
    elif info[0] == 3 and not info[1] >= 3:
        print('Python 3.3+ required')
        sys.exit(1)
    elif info[0] not in [2, 3]:
        print('Python version not supported')
        sys.exit(1)
    else:
        print(info)
        sys.exit(1)


if __name__ == '__main__':
    # check_python()

    b = [a*2 for a in [1, 2, 3]]
    print(b)
    g = lambda x, y: print((x + 1)*y)
    g(4, 5)
    xFn = lambda _: True, 0
    print(xFn[0])