try :
    a = int(input("Enter the First Number :"))
    b = int(input("Enter the Second Number :"))

    print("what type of operation you perform \npress + for Addition\npress - for Substraction\npress * for multipition \npress / for divide")

    o= input("Enter the Operation : ")
    match o :
        case "+":
            print(f"The result is : {a+b}")
        case "-":
            print(f"The result is : {a-b}")
        case "*":
            print(f"The result is : {a*b}")
        case "/":
            print(f"The result is : {a/b}")
        case defult:
            print("there was a error")

except Exception as e :
    print("Enter the valid value of a and b ")