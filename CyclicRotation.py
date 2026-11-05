def solution (A, K):
    for i in range(K):
        temp = A.pop() # Remove the last element from the array and store it
        A.insert(0, temp) # Add the removed element to the beginning of the array
    return A
