import re

class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        num_list = re.split(r",|\n", numbers)  # Split by comma or newline
        return sum(int(num) for num in num_list)
