def binarysearch(array, search_element):
    high = len(array)
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == search_element:
            return mid
        elif search_element < array[mid]:
            high = mid - 1
        else:
            low = mid + 1   
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = 5
result = binarysearch(array, search_element)
if result != -1 :
    print(f"{search_element} found at index: {result}")        
else:
    print( "{search_element} not found")      