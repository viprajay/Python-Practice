num1 = int(input("Enter the First num : "))
num2 = int(input("Enter the Second num : "))
i=1
while(i<=num1 and i<=num2):
    if(num1%i==0 and num2%i==0):
        gcd=i
    i = i+1
print("GCD : ",gcd)
