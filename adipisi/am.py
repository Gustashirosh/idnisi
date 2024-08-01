def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(current):
    next_num = current + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1

# Example usage
current_number = 10
next_prime_number = next_prime(current_number)
print(f"The next prime number after {current_number} is {next_prime_number}")
