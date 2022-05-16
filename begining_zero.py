#Вам дана строка состоящая только из цифр. 
#Вам нужно посчитать сколько нулей ("0") находится в начале строки.
#Входные данные: Строка, состоящая только из цифр.
#Выходные данные: Целое число.
def beginning_zeros(number: str) -> int:
    # your code here

    # Если в строке одни нули
    if number == '0'*(len(number)):
        return len(number)
    # к обычному числу
    num_reverse = "".join(reversed(number))
    num_int = int(num_reverse)
    count = 0
    while num_int > 0:
        if num_int % 10 == 0:
            count += 1
            num_int = num_int / 10
        else:
            break
    return count


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")