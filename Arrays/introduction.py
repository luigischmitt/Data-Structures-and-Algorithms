# Introduction

strings = ['a', 'b', 'c', 'd'] # 4*4 = 16 bytes of storage

print(strings[2]) # Access - O(1)

strings.append('e') # Insert at the end - O(1) 

strings.pop() # Delete the final element - O(1)

strings.insert(0, 'x') # Insert at the beggining - O(n), looping through all elements

strings.insert(2, 'alien') # Insert at the middle of the array - O(n/2), but removing the constans we have O(n)

print(strings) 

# Static vs Dynamic Arrays - In Python arrays are Dynamic, so the language realocate the memory for you, you don't need to worry about that
