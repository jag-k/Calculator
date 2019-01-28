from functools import wraps


def annotation(func):
    @wraps(func)
    def _(*args, **kwargs):
        _.__doc__ = func.__name__.upper() + (" WITH " + str(args)[1:-2]
                                             if args else "")
        return func(*args, **kwargs)
    return _


@annotation
def concat(num: int) -> int:
    @wraps(concat)
    def _(res: int) -> int:
        return int(f"{res}{num}")
    return _


@annotation
def addition(num: int) -> int:
    @wraps(addition)
    def _(res: int) -> int:
        return res + num
    return _


@annotation
def division(num: int) -> int:
    @wraps(division)
    def _(res: int) -> int:
        return res // num
    return _


@annotation
def multiplication(num: int) -> int:
    @wraps(multiplication)
    def _(res: int) -> int:
        return res * num
    return _


@annotation
def reverse() -> int:
    @wraps(reverse)
    def _(res: int) -> int:
        return int(''.join(reversed(str(res))))
    return _

