def getValues(filename):
    with open(filename) as f:
        m, n = map(int, f.readline().split())
        pizzas = list(map(int, f.readline().split()))

    return m, n, pizzas


def closest2diff(iterable, diff):
    diffs = list(map(lambda x: abs(diff - x), iterable))
    diffs.reverse()
    closest = 1 - diffs.index(max(diffs))

    return closest


def getSlices(pizzas, maxi):
    c_pizzas = pizzas.copy()
    _sum = sum(c_pizzas)
    diff = _sum - maxi

    print(_sum)
    input()

    while _sum > maxi:
        index = closest2diff(c_pizzas, diff)
        _sum -= c_pizzas[index]
        c_pizzas[index] = 0
        print(_sum)

    return c_pizzas


if __name__ == "__main__":
    filename = 'data/b_small.in'
    m, n, pizzas = getValues(filename)
    print(getSlices(pizzas, m))

    

