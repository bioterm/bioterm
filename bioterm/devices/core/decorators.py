from functools import wraps


def rpc(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    wrapper.is_rpc = True
    return wrapper


def crpc(f):
    f.is_rpc = True
    return f
