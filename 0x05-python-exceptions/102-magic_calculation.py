def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result = (a ** b) / i + result
        except Exceptions as e:
            result = b + a
    return (result)
