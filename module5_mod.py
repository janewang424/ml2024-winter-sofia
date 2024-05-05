class InputNum:
    def __init__(self):
        self.numbers = []
    
    def add_number(self, num):
        self.numbers.append(num)
    
    def find_index(self, target):
        try:
            return self.numbers.index(target) + 1  # index from 1-N
        except ValueError:
            return -1