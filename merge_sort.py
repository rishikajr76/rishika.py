def merge(numbers, low, mid, high):
    arr1 = numbers[low : mid+1]
    arr2 = numbers[mid+1 : high+1]

    i = 0
    j = 0
    k = low
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            numbers[k] = arr1[i]
            i += 1
        else:
            numbers[k] = arr2[j]
            j += 1
        k += 1
    numbers[k:high+1] = arr1[i:] + arr2[j:]
    # numbers[k:high+1] = arr2[j:]

def merge_sort(numbers, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(numbers, low, mid)
        merge_sort(numbers, mid+1, high)
        merge(numbers, low, mid, high)

print('Enter the input numbers: ')
numbers = [int(num) for num in input().split()]

merge_sort(numbers, 0, len(numbers)-1)
print('Sorted Numbers are \n', numbers)
