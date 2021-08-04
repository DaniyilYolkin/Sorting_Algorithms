def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    
    else:
        items_lower = []
        items_higher = []
        pivot = arr.pop()
        for item in arr:
            if item < pivot:
                items_lower.append(item)
            
            else:
                items_higher.append(item)
        return quick_sort(items_lower) + [pivot] + quick_sort(items_higher)


print(quick_sort([5, 2, 4, 6, 1, 3]))