import re

class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        
        delimiter = ",|\n"  # Default delimiters
        
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split("\n", 1)
            delimiter = re.escape(delimiter)
        
        num_list = re.split(delimiter, numbers)
        num_list = [int(num) for num in num_list]
        
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")
        
        return sum(num_list)
