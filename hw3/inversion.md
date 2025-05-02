function Inversion(arr, left, right):
    if left >= right:
        return 0
    
    middle = (left + right) // 2

    inversions = Inversion(arr, left, middle)
    inversions += Inversion(arr, middle + 1, right)
    i = left
    j = middle + 1
    interInversions = 0
    newArray = []

    while i <= middle && j<= right:
        if arr[i] <= arr[j]:
            newArray.append(arr[i])
            i += 1
        else:
            newArray.append(arr[j])
            j += 1
            interInversions += (middle - i + 1)
    
    while i <= middle:
        newArray.append(arr[i])
        i += 1
    while j <= right:
        newArray.append(arr[j])
        j += 1
    for k in range(0, newArray.length()):
        arr[left + k] = newArray[k]
        
    return inversions + interInversions
