def get_data():
    with open(FILENAME) as f:
        B, L, D = map(int, f.readline().split())
        books = dict(enumerate(map(int, f.readline().split())))
        libraries = {}
        for i in range(L):
            libraries[i] = {}
            libraries[i]['num_books'], libraries[i]['sign_days'], libraries[i]['book_per_day'] = list(map(int, f.readline().split()))
            libraries[i]['books'] = list(map(int, f.readline().split()))

        
    return B, L, D, books, libraries


