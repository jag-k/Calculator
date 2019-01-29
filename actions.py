from functools import wraps


def annotation(func):
    def dec(*args, **kwargs):
        @wraps(func)
        def _(res: int):
            _.__doc__ = func.__name__.upper() + (" WITH " + str(args)[1:-2]
                                                 if args else "")
            return int(func(res, *args, **kwargs))

        return _

    return dec


@annotation
def concat(res: int, num: int):
    return f"{res}{num}"


@annotation
def addition(res: int, num: int):
    return res + num


@annotation
def division(res: int, num: int):
    return res // num


@annotation
def multiplication(res: int, num: int):
    return res * num


@annotation
def replace(res: int, old: int, new: int):
    return str(res).replace(str(old), str(new))


@annotation
def reverse(res: int):
    return int(''.join(reversed(str(res))))


@annotation
def delete(res: int):
    return str(res)[:-1]
