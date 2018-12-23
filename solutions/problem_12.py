from tools import get_factors, get_triangle_number, run_euler

@run_euler
def get_triangle_with_factors_more_than(i):
    n = 1

    while True:
        triangle = get_triangle_number(n)
        factors = get_factors(triangle)
        if len(factors) > i:
            return triangle
        else:
            n += 1


get_triangle_with_factors_more_than(500)
