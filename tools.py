import time

def run_euler(func):
    def wrapper(*arg, **kwargs):
        t1 = time.time()
        answer = func(*arg, **kwargs)
        t2 = time.time()
        print('Answer: {answer}\nTime (s): {time:0.2f}'.format(
            answer=answer,
            time=t2 - t1
        ))
    return wrapper


def get_triangle_number(n):
    return int(n * (n + 1) / 2)


def get_factors(n):
    factors = []
    limit = int(n ** 0.5)

    for i in range(1, limit + 1):
        if n % i == 0:
            factors += [n // i, i]
    return set(factors)


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True
