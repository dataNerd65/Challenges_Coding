class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Converting all integers to strings
        str_p = [str(num) for num in digits]
        # Joining the list to a single string and convert to an integer then add 1
        incremented_number = int(''.join(str_p)) + 1

        # Convert the resulting number back to a list of digits
        return [int(digit) for digit in str(incremented_number)]

        