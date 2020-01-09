from itertools import combinations as comb

def getValues(filename):
    with open(filename) as f:
        m, n = map(int, f.readline().split())
        pizzas = list(map(int, f.readline().split()))
        f.close()

    return m, n, pizzas


def getSlices(pizzas, maxi):
    best, bestSum = [], 0
    copy_p = pizzas.copy()
    for i in range(1, len(pizzas)):
        copy = pizzas.copy()
        arrangements = list(comb(copy, i))
        for x in arrangements:
            if maxi >= sum(x) > bestSum:
                bestSum = sum(x)
                best = x
    indices = []
    for i in best:
        index = copy_p.index(i)
        indices.append(index)
        copy_p[index] = 0
    
    print(bestSum)
    return indices


if __name__ == "__main__":
    files = ['a_example.in', 'b_small.in']
    for filename in files:
        m, n, pizzas = getValues('data/' + filename)
        print(filename, m, sep='\n')
        slices = getSlices(pizzas, m)
        with open('output/output_' + filename, 'w') as f:
            f.write(str(len(slices)) + '\n')
            f.write(' '.join(map(str, slices)))
            f.close()


    

