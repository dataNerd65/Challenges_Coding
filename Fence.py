def find_min_height_fence(heights, k):
    n = len(heights)
    if n < k:
        return -1  # Not enough planks to form a segment of length k

    # Initial sum of the first k planks
    min_height_sum = sum(heights[:k])
    current_height_sum = min_height_sum
    min_index = 0

    # Sliding window
    for i in range(1, n - k + 1):
        # Update the sum by sliding the window
        current_height_sum = current_height_sum - heights[i - 1] + heights[i + k - 1]

        # Check if the current sum is less than the minimum sum found so far
        if current_height_sum < min_height_sum:
            min_height_sum = current_height_sum
            min_index = i

    return min_index

# Example usage
heights = [1, 3, 2, 4, 5, 1, 2, 1, 6]
k = 3
min_index = find_min_height_fence(heights, k)
print(f"The starting index of the segment with minimum height sum is: {min_index}")
