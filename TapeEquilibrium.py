def solution(A):
    left_sum = A[0]
    right_sum = 0

    # Calculate the sum of all elements to the right of the initial split
    for i in range(len(A) - 1):
        right_sum += A[i + 1]

    # Calculate the difference at the initial split
    diff = abs(left_sum - right_sum)
    smallest_diff = diff

    # Move the split point right, keeping at least one element on each side
    for i in range(1, len(A) - 1):
        left_sum += A[i]  # Add the current element to the left partition
        right_sum -= A[i]  # Remove the same element from the right partition

        diff = abs(left_sum - right_sum)  # Calculate the difference at the new split

        # Update the minimum if the new split produces a smaller difference
        if diff < smallest_diff:
            smallest_diff = diff

    return smallest_diff
