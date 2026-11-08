def solution (A, K):
    if not A: return A # Return array if it is empty
    for i in range(K):
        temp = A.pop() # Remove the last element from the array and store it
        A.insert(0, temp) # Add the removed element to the beginning of the array
    return A
