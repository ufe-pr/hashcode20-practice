from operator import itemgetter


def get_data(FILENAME):
    with open(FILENAME) as f:
        B, L, D = map(int, f.readline().split())
        books = dict(enumerate(map(int, f.readline().split())))
        libraries = {}
        for i in range(L):
            libraries[i] = {}
            libraries[i]['num_books'], libraries[i]['sign_days'], libraries[i]['book_per_day'] = list(map(int, f.readline().split()))
            libraries[i]['books'] = sorted(list(map(int, f.readline().split())), reverse=True)
            libraries[i]['s_books'] = []

        
    return B, L, D, books, libraries
def sort_by_days(libraries, L):
    ds = []
    for i in range(L):
        ds.append(libraries[i]['sign_days'])

    group = zip(ds, range(L))
    sort = sorted(group)
    return [x[1] for x in sort]


def signup_order(L, libraries):

    return sort_by_days(libraries, L)


def get_books_per_day(libraries, books, D):
    SB = []
    AL = set()
    lib_order = signup_order(len(libraries), libraries)
    last_sum = -1
    last_index = 0
    complete_days = []

    for i in lib_order:
        last_sum += libraries[i]['sign_days']
        complete_days.append(last_sum)
    
    for i in range(D):
        to_remove = []
        for lib_i in AL:
            lib = libraries[lib_i]
            bpd = lib['book_per_day']
            s_count = 0
            index = 0
            num_books = lib['num_books']
            if not num_books > len(lib['s_books']):
                to_remove.append(lib_i)
                continue
            while s_count < bpd and num_books > len(lib['s_books']) and index < len(lib['books']):
                book = lib['books'][index]
                if book not in SB:
                    SB.append(book)
                    lib['s_books'].append(book)
                    lib['books'].remove(book)
                    s_count += 1
                index += 1
        if i in complete_days:
            AL.add(lib_order[complete_days.index(i)])
        for o in to_remove:
            AL.remove(o)
        print('End of day', i)

    outputs = []
    out_count = 0

    for i in lib_order:
        s_books = libraries[i]['s_books']
        if len(s_books) > 0:
            outputs.append([i, len(s_books), s_books])
            out_count += 1

    return out_count, outputs
        
FILENAMES = ['c_incunabula.txt']

for i in FILENAMES:
    FILENAME = i
    B, L, D, books, libraries = get_data(FILENAME)
    out_c, outs = get_books_per_day(libraries, books, D)

    with open(FILENAME + '.out', 'w') as f:
        f.write(str(out_c) + '\n')
        for i in outs:
            if i[1] > 0:
                f.write('{} {}\n'.format(i[0], i[1]))
                f.write(' '.join(map(str, i[2])) + '\n')

    