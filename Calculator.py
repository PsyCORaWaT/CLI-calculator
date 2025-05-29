print("Welcome to the Calculator ")

Name = input("Please Enter Ur name ")

print(f"Hey! {Name} Please Choose one Opeator ")

a = float(input("Enter the First Number "))
b = float(input("Enter the Second Number "))

oper = str(input("+, -, *, /"))


if oper== "+":
    print(a+b)
elif oper=="-":
    print(a-b)
elif oper=="*":
    print(a*b)
elif oper=="/":
    print(a/b)
else:
        print("You Chose a Wrong Operator. \n Please run Code again and Choose from '+, -, *, /' ")

