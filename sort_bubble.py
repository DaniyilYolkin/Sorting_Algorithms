def bubble_sort(arr):
    swapped = True
    while swapped == True:
        swapped = False
        for j in range(0, len(arr)-1):
            key = arr[j]
            if key > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = key
                swapped = True
    return arr
print(bubble_sort([5, 2, 4, 6, 1, 3]))