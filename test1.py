
from test0 import Greeter, sum111, aaaa

def something(a, b):
    # Create an instance of Greeter
    greeter = Greeter("Alice")
    # Call the greet method
    greeter.greet()
    
    sum_value = sum111(a, b)
    dict_value = aaaa[1]
    result = sum_value + dict_value

    return result

if __name__ == "__main__":
    print(something(1, 2))