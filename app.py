def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def format_result(operation, a, b, result):
    return f"{operation}({a}, {b}) = {result}"

def run_demo():
    outputs = []
    outputs.append(format_result("add", 2, 3, add(2, 3)))
    outputs.append(format_result("subtract", 5, 2, subtract(5, 2)))
    outputs.append(format_result("multiply", 4, 3, multiply(4, 3)))
    return outputs

if __name__ == "__main__":
    for line in run_demo():
        print(line)
