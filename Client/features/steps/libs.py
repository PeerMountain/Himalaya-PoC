def ghernik_vars(func):
    "Decorator to change interpretation of certain strings."
    def wrapper(context, *args, **kwargs):
        args = [
            getattr(context, arg[1:-1]) if (
                arg.startswith('[') and arg.endswith(']')
            )
            else arg for arg in args
        ]
        return func(context, *args, **kwargs)
    return wrapper
