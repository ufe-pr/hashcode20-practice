from itertools import *
link = "data/c_medium.in"
path = open(link, "r")
firstLine = path.readline().split()
maxNum, pizzaNum = int(firstLine[0]), int(firstLine[1])
pizzas = path.readline().split()
pizzas, iterations = [int(x) for x in pizzas], []
summation, move, check, move1 = 0, 0, 0, 0
while summation < maxNum:
    summation += pizzas[move]
    move += 1
print(summation, move)

while check < summation-maxNum:
    check = pizzas[move1]
    move1 += 1
print(check, move1)
indexes = list(range(move))

indexes.remove(move1-1)
m = 0
for i in indexes:
    m += pizzas[i]
print(m)


# print(indexes[5461])

# for i in range(2, len(pizzas)+1):
#     iterations += (x for x in set(combinations(pizzas, i)))
# sums, guide = [sum(x) for x in iterations], 0
# for i in sums:
#     if guide < i <= maxNum:
#         guide = i
#     else: pass
# final = []
# for x in set(iterations):
#     if sum(x) == guide:
#         print(x)
#         final += [x]
# indexes = [pizzas.index(x) for x in final[0]]
# print(final)
with open('also_big.out', 'w') as f:
    f.write(str(len(indexes))+'\n')
    for i in indexes:
        f.write(str(i) + ' ')




