add = lambda a,b:a+b
sub = lambda a,b:a-b
mul = lambda a,b:a*b
div = lambda a,b:a/b
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = input("Enter the operation(+-*/):")
match c:
    case "+":
        print(add(a,b))
    case "-":
        print(sub(a,b))
    case "*":
        print(mul(a*b))
    case "/":
        print(div(a,b))
