from functools import wraps


def annotation(func):
    def dec(*args, **kwargs):
        @wraps(func)
        def _(res: float):
            _.__doc__ = func.__name__.upper() + (" WITH " + str(args)[1:-2]
                                                 if args else "")
            return float(func(res, *args, **kwargs))

        return _

    return dec


@annotation
def concat(res: float, num: float):
    return f"{res}{num}"


@annotation
def addition(res: float, num: float):
    return res + num


@annotation
def division(res: float, num: float):
    return res / num


@annotation
def multiplication(res: float, num: float):
    return res * num


@annotation
def replace(res: float, old: int, new: int):
    return str(res).replace(str(old), str(new))


@annotation
def reverse(res: float):
    return int(''.join(reversed(str(res))))


@annotation
def delete(res: float):
    return str(int(res))[:-1]
