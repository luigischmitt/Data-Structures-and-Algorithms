# O(n) Time | O(n) Space - Solution
def sortedSquaredArray(array):
    result = [0 for _ in array]
    i = len(result) - 1
    l = 0
    r = len(array) - 1
    while l <= r:
        if abs(array[r]) >= abs(array[l]):
            result[i] = array[r] * array[r]
            r -= 1
        else:
            result[i] = array[l] * array[l]
            l += 1
        i -= 1
    return result

print(sortedSquaredArray([-7,-5,-4, 1, 2, 9, 11]))
