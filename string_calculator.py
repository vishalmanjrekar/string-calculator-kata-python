import re

class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        
        delimiter = ",|\n"  # Default delimiters
        
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split("\n", 1)  # Extract custom delimiter
            delimiter = re.escape(delimiter)  # Escape special characters for regex
        
        num_list = re.split(delimiter, numbers)
        return sum(int(num) for num in num_list)
