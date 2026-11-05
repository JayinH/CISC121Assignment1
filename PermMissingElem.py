def solution(A):
    total_nums = len(A) + 1

    # Use gauss summation to add all numbers from 1 to the length of A + 1
    predicted_total = (total_nums * (total_nums + 1)) // 2  

    total = 0

    for n in A:
        total += n # Total stores sum of all numbers in array

    missing_num = predicted_total-total 
    return missing_num
