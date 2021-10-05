def controller_setter(func):
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            return val
        except BaseException as b_e:
            args[0].show_error(b_e)

    return wrapper
