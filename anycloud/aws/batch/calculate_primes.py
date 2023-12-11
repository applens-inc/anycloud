def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculate_primes(start, end):
    primes = [num for num in range(start, end) if is_prime(num)]
    return primes


if __name__ == "__main__":
    start_range = 1000000
    end_range = 1010000
    primes = calculate_primes(start_range, end_range)
    print(primes)
