sorted_arr = []
def selection_sort(arr):
    global sorted_arr
    if len(arr) == 1:
        return sorted_arr + [arr[0]]

    else:
        sorted_arr.append(min(arr))
        arr.remove(min(arr))
        return selection_sort(arr) 

print(selection_sort([5, 2, 4, 6, 1, 3]))