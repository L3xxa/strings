

def _search(a,b):
    search = 0
    for i in a:
        if i == b:
            search += 1
    if search == 0:
        print(f"Кількість символів що ви шукали = 0")
    else:
        print(f"Кількість символів що ви шукали = {search}")
    return search



