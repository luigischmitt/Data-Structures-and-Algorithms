# Leet Code - 88. Merge Sorted Array

# Easy, but not good way for interviews
def merge(arr1, arr2):
    aux = arr1 + arr2
    aux.sort()

    return aux

arr1 = [0, 1, 3, 5]
arr2 = [2, 4, 6]

print(merge(arr1, arr2))

# My first try to overcome this problem
def merge2(arr1, arr2):
    aux = []

    while (len(arr1) > 0 and len(arr2) > 0):
        if (arr1[0] <= arr2[0]):
            aux.append(arr1[0])
            arr1.pop(0)
        else:
            aux.append(arr2[0])
            arr2.pop(0)

    if (len(arr1) > 0 or len(arr2) > 0):
        aux += arr1
        aux += arr2

    return aux

print(merge2(arr1, arr2))

# Constraints: it modify the data of arr1 and arr2 and in large arrays it will be O(n²), because pop() shifts the array everytime

arr1 = [0, 1, 3, 5]
arr2 = [2, 4, 6]

# A better version - O(n + m) time complexity
def merge3(arr1,arr2):
  if len(arr1) == 0 or len(arr2) == 0:
    return arr1 + arr2
  
  mylist = []
  i = 0
  j = 0

  while (i < len(arr1) and j < len(arr2)):

    if (arr1[i] <= arr2[j]):
      mylist.append(arr1[i])
      i+=1
    elif (arr2[j] < arr1[i]):
      mylist.append(arr2[j])
      j+=1

  return mylist + arr1[i:] + arr2[j:] # This ensures that no elements are left out, even if the arrays have different sizes

print(merge3(arr1, arr2))
