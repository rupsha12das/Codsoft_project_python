def add(numbers):
   result=sum(numbers)  
   expr="+".join(str(int(n))if n.is_integer()
else str(n)for n in numbers)   
   return f"{expr}={int(result) if result.is_integer() else result}"
def subtract(numbers):
    result=numbers[0]
    for num in numbers[1:]:
        result-=num
    expr="-".join(str(int(n))if n.is_integer()
else str(n)for n in numbers)   
    return f"{expr}={int(result) if result.is_integer() else result}"
def multiply(numbers):
    result=1
    for num in numbers:
        result*=num
    expr="*".join(str(int(n))if n.is_integer()
else str(n)for n in numbers)   
    return f"{expr}={int(result) if result.is_integer() else result}"
def divide(numbers):
    result=numbers[0]
    try:
        for num in numbers[1:]:
            result/=num
    except ZeroDivisionError:
        return "Cannot divide by zero"    
     
    expr="/".join(str(int(n))if n.is_integer()
else str(n)for n in numbers)   
    return f"{expr}={int(result) if result.is_integer() else result}" 
  
print("Multiple Number Calculator:   ")
while True:
    print("---------Choose Operation-------")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit")
    choice=int(input("Enter a choice 1/2/3/4/5:  "))
    if choice==5:
        print("Quit")
        break
    if choice in(1,2,3,4):
        try:
            numbers=input("Enter numbers separated by spaces: ")
            numbers=[float(num)for num in numbers.split()]    
            if len(numbers)<2:
                print("Enter at least two numbers:")
                continue
        except ValueError:
            print("Invalid inputs")  
            continue      
        if choice==1:
            print(add(numbers))
        elif choice==2:
            print(subtract(numbers))
        elif choice==3:
            print(multiply(numbers))    
        elif choice==4:
            print(divide(numbers))  
        elif choice==5:
            print("Quit")    