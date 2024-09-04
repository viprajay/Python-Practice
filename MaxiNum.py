def find_maximum(numbers):
    if not numbers:
        return None  
    max_num = numbers[0]  
    for num in numbers[1:]:  
        if num > max_num:
            max_num = num  
    return max_num

numbers_list = [20, 5, 8, 29, 15]
print("Maximum number: ", find_maximum(numbers_list))
