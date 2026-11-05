def solution (X, Y, D):
    distance = Y - X  # Calculate the distance the frog needs to travel
    adjusted_distance = distance + D - 1  # Adjust the distance to round up partial jumps
    jumps = adjusted_distance // D  # Use integer division to find the minimum number of jumps
    return jumps
