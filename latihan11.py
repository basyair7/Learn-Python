# Implementasi Array dengan Python

def test1():
    var_arr = [0 for i in range(10)]
    print(var_arr)

def test2():
    var_arr = [0 for i in range(10)]

    for i in range(10):
        var_arr[i] = i
        
    print(var_arr)

def test3():
    var_arr = [1, 2, 3, 4, 5]

    for i in range(len(var_arr)):
        current_element = var_arr[i]
        next_index = i+1
        
        if next_index < len(var_arr):
            next_element = var_arr[next_index]
        else:
            next_element = None
            
        print(f"Current element: {current_element}, next elements: {next_element}")

def test4():
    var_arr = [1, 7, 2, 89, 3]
    left_pointer = var_arr[1]

    for i in range(1, len(var_arr)):
        right_pointer = var_arr[i]
        if right_pointer > left_pointer:
            boolean = True
            print(f"{right_pointer} > {left_pointer} = {boolean}")
        else:
            boolean = False
            print(f"{right_pointer} > {left_pointer} = {boolean}")

def test5():
    var_array = [i for i in range(1, 101)]
    total = sum(var_array)
    result = total / len(var_array)
    print(result)

def test6():
    var_array = [i for i in range(1, 101)]
    print(sum_array(var_array))    

def sum_array(value: list):
    total = 0
    for num in value:
        total += num
    return total /  len(value)


# test1()
# test2()
# test3()
# test4()
# hasil test 5 dan 6 sama
# test5()
test6()