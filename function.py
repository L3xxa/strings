
def calculator(mini_calculator):
    data = []
    for i in mini_calculator:
        if i.isdigit():
            data.append(i)
        else:
            data.append(i)
    if data[1] == "+":
        data = int(data[0]) + int(data[2])
    elif data[1] == "-":
        data = int(data[0]) - int(data[2])
    elif data[1] == "*":
        data = int(data[0]) * int(data[2])
    elif data[1] == "/":
        data = int(data[0]) / int(data[2])
    else:
        data = "Invalid Operator"
    return  data

