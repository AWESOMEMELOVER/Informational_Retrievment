DOCS_QUANTITY = 27


def my_and(x, y):
    if isinstance(x, set) and isinstance(y, set):
        return x.intersection(y)
    elif isinstance(x, list) and isinstance(y, list):
        return x and y


def my_or(x, y):
    if isinstance(x, set) and isinstance(y, set):
        return x.union(y)
    elif isinstance(x, list) and isinstance(y, list):
        return x or y


def my_not(x):
    if isinstance(x, set):
        return set(range(DOCS_QUANTITY)).difference(x)
    elif isinstance(x, list):
        return [0 if i == 1 else 1 for i in x]


if __name__=='__main__':
    test1 = [1, 1, 0]
    test2 = [1, 0, 1]
    print(type(test1))
    print(my_or(test1, test2))

