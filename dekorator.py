import functools

def log_types(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        param_info = []
        for i, arg in enumerate(args):
            param_info.append(f"arg{i}: {type(arg).__name__}")
        for key, value in kwargs.items():
            param_info.append(f"{key}: {type(value).__name__}")
        print(f"Logging: {func.__name__}({', '.join(param_info)})")
        return func(*args, **kwargs)
    return wrapper

@log_types
def example_function(a: int, b: str, c: float):
    return f"Received: {a}, {b}, {c}"

# Przykładowe wywołanie
example_function(10, "hello", 3.14)