from collections import defaultdict

def find_optimal_height(heights):
    # Dictionary to store the frequency of each height
    height_freq = defaultdict(int)
    
    # Calculate the frequency of each height
    for height in heights:
        height_freq[height] += 1

    # Find the height with the maximum frequency
    max_frequency = 0
    optimal_height = heights[0]
    
    for height, freq in height_freq.items():
        if freq > max_frequency:
            max_frequency = freq
            optimal_height = height

    return optimal_height, max_frequency

# Example usage
heights = [1, 3, 2, 4, 5, 1, 2, 1, 6]
optimal_height, max_frequency = find_optimal_height(heights)
print(f"The optimal height to adjust planks is: {optimal_height} with {max_frequency} planks.")
