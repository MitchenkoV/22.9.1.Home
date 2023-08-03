def binary_search(array, chislo, left, right):
    if left > right:  
            return False
    middle = (right + left) // 2
    if chislo == array[middle]:
        if array[middle - 1] < chislo and chislo <= array[middle]:  
            return middle
        elif chislo < array[middle]:  
            
            return binary_search(array, chislo, left, middle - 1)
    elif chislo == array[middle - 1]:  
        
            return binary_search(array, chislo, left, middle - 1)
    else:  
            return binary_search(array, chislo, middle + 1, right)
array = list(map(int, input("Введите несколько целых чисел через пробел: ").split()))
chislo = int(input("Введите любое случайное число в диапазоне введенных чисел: "))
array = sorted(array)
print(array)
left = int(array[0])
right = int(array[-1])
if chislo < left or chislo > right:
    print('Числа нет в диапазоне')
else:
    print(binary_search(array, chislo, 0, len(array) - 1))