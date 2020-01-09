from itertools import combinations as comb

def getValues(filename):
    with open(filename) as f:
        m, n = map(int, f.readline().split())
        pizzas = list(map(int, f.readline().split()))
        f.close()

    return m, n, pizzas


def getInd2Rem(pizzas, diff, indices):
    vals = [pizzas[x] for x in indices]
    best = vals[0]
    for i in vals:
        if i > diff:
            excess = i - diff
            rem = diff - best
            if min(vals) > (excess + rem):
                return indices[vals.index(i)]
            break
        best = i
    return indices[vals.index(best)]

def getSlices(pizzas, maxi):
    _sum = 0
    current = 0
    indices = []
    while _sum <= maxi:
        _sum += pizzas[current]
        indices.append(current)
        current += 1

    diff = _sum - maxi
    while _sum > maxi:
        ind2rem = getInd2Rem(pizzas, diff, indices)
        _sum -= pizzas[ind2rem]
        indices.remove(ind2rem)
        diff = _sum - maxi
    
    return indices

def iterate(pizzas, indices, excess, rem):
    best = ((), rem)
    for i in range(1, min(3, len(indices)) + 1):
        arrs = comb(indices, i)
        for i in arrs:
            _sum = sum(map(lambda x: pizzas[x], i))
            if _sum >= excess and (_sum - excess) < best[1]:
                best = (i, _sum - excess)

        if best[1] == 0:
            break

    return best[1] == 0, best
                

def selectSlices(pizzas, maxi, indices, countdown=100):
    print(countdown)
    filteredList = pizzas.copy()
    myIndices = set(indices)
    rem = maxi - sum(map(lambda x: pizzas[x], indices))
    for i in indices:
        filteredList[i] = 0
    for i in filteredList:
        if i != 0:
            # print(i)
            excess = i - rem
            index = filteredList.index(i)
            perfect, best = iterate(pizzas, indices, excess, rem)
            if best[0]:
                list(map(lambda x: myIndices.remove(x), best[0]))
                myIndices.add(index)
            if perfect or not countdown:
                return list(myIndices)
    else:
        return list(myIndices)

            
    return selectSlices(pizzas, maxi, myIndices, countdown - 1)


if __name__ == "__main__":
    files = ['c_medium.in', 'd_quite_big.in', 'e_also_big.in']
    for filename in files:
        m, n, pizzas = getValues('data/' + filename)
        print(filename, m, sep='\n')
        slices = getSlices(pizzas, m)
        slices = selectSlices(pizzas, m, slices)
        print(sum(map(lambda x: pizzas[x], slices)))
        with open('output/output_' + filename, 'w') as f:
            f.write(str(len(slices)) + '\n')
            f.write(' '.join(map(str, slices)))
            f.close()

