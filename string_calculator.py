class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        num_list = numbers.split(',')
        if len(num_list) == 1:
            return int(num_list[0])
        return int(num_list[0]) + int(num_list[1])