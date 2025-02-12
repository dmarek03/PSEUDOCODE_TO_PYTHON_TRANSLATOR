print("Enter a number: ")
NumA = input("Enter data: ")
print("Enter another number: ")
NumB = input("Enter data: ")
NumA = float(NumA)
NumB = float(NumB)
print("Enter operator: ")
Operator = input("Enter data: ")
match Operator:
    case "add":
        print(f"{(NumA + NumB)}")
    case "sub":
        print(f"{(NumA - NumB)}")
    case "mul":
        print(f"{(NumA * NumB)}")
    case "div":
        print(f"{(NumA / NumB)}")
    case "mod":
        print(f"{(NumA % NumB)}")
    case _:
        print("Unknown operator")
