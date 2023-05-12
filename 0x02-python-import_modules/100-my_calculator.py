#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    result = 0
    match operator:
        case '+':
            result = add(a, b)
        case '-':
            result = sub(a, b)
        case '*':
            result = mul(a, b)
        case '/':
            result = div(a, b)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))