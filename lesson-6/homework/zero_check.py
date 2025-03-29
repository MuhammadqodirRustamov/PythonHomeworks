def check(func):
    def wrapper(a,b):
        try:
            res = func(a,b)
            return res
        except ZeroDivisionError:
            return "Denominator can not be zero"
    return wrapper

@check
def div(a, b):
    return a / b

print(div(6,0))