def solution(A):
    unpaired = 0

    for num in A:
        unpaired ^= num # Use xor operator which fips matching bits to 0, while unique bits pass through unchanged

    return unpaired
