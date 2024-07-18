def field(value):
    # Perform some operation on the value
    # Example:
    return value * 2

class Wrapper:
    def __init__(self, data, i1):
        self.data = data
        self.i1 = i1

# Example usage
data = [10, 20, 30, 40, 50]
w = Wrapper(data, 3)

result = field(w.data[w.i1 - 1])
print(result)  # Output: 60 (30 * 2)
