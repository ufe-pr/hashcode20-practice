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

def signup_order(L):
    return list(range(L))


def get_books_per_day(libraries, books, D):
    SB = []
    AL = set()
    lib_order = signup_order(len(libraries))
    
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
        ssum = 0
        for lib_index in lib_order:
            ssum += libraries[lib_index]['sign_days']
            if ssum <= i + 1:
                AL.add(lib_index)
        for i in to_remove:
            AL.remove(i)
        print('End of day', i)

    outputs = []
    out_count = 0

    for i in lib_order:
        s_books = libraries[i]['s_books']
        if len(s_books) > 0:
            outputs.append([i, len(s_books), s_books])
            out_count += 1

    return out_count, outputs
        
FILENAMES = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt', 'd_tough_choices.txt', 'e_so_many_books.txt', 'f_libraries_of_the_world.txt']

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

    