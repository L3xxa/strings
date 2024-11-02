from function import _list


a = input("Enter numbers separated by spaces: ")
try:
    number_list = [int(num) for num in a.split()]
except ValueError:
    print("Invalid input. Please enter only numbers separated by spaces.")
    exit()

result,minus,zero = _list(number_list)
data = result

print(f' Sort list{result}')
print(f' The maximum value of the list: {data[-1]}')
print(f' The minimum value of the list: {data[0]}')
print(f'Number of negative numbers: {minus}')







