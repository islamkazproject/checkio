#У вас есть число и нужно определить какая цифра из этого числа является наибольшей.
#Входные данные: Положительное целое число.
#Выходные данные: Целое число (0-9).
from itertools import count


def max_digit(number: int) -> int:
    # your code here
    num_list = [] # List
    max_num = 0 # max count
    # Исключаем 0
    if not number:
        return number
    # Число дробим на числа и записываем в список
    while number > 0:
        num = number % 10
        num_list.append(num)
        number = number // 10     
    # Сравниваем числа в списке
    """
    count = 0 #Счетчик для чикла
    i = 0
    while count != (len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            i = i + 1 
            count += 1
            max_num == num_list[i]
            return max_num
        else:
            max_num == num_list[i+1]
            return max_num
            """
    return max(num_list)        
if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
