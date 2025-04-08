def sum_arr(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_arr(arr[1:])


print(sum_arr([1, 2, 3]))

def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([34, 2, 67, 3, 12, 0, 22]))
