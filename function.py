def _list(number_list):
    data = []
    minus = 0
    zero = 0
    for i in number_list:
        data.append(i)
        if i < 0:
            minus += 1
        if i == 0:
            zero += 1

    data.sort()
    return data, minus, zero




