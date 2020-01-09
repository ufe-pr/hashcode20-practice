from slice import getValues
def check(data_file, output_file):
    m, n, pizzas = getValues(data_file)
    with open(output_file) as out:
        num_pizzas = int(out.readline())
        indices = list(map(int, out.readline().split()))
        amount_slices = sum(map(lambda x: pizzas[x], indices))
        if amount_slices <= m and len(indices) == len(set(indices)):
            print(amount_slices)
            return True
    return False

if __name__ == "__main__":
    data_files = ['c_medium.in', 'd_quite_big.in', 'e_also_big.in'] + ['a_example.in', 'b_small.in']
    output_files = list(map(lambda x: 'output_'+ x, data_files))
    for data, output in zip(data_files, output_files):
        if not check('data/' + data, 'output/' + output):
            print(data, 'was incorrect', output)