print("Choose your operation")
print("+   -   *   %   /  exp  sqrt")
n=input()
print("Enter two inputs with a space")
a,b=map(int,input().split())
if(n=='+'):
    print(a+b)
elif(n=='-'):
    print(a-b)
elif(n=='*'):
    print(a*b)
elif(n=='%'):
    print(a%b)
elif(n=='/'):
    print(a//b)
elif(n=='exp'):
    print(a**b)
elif(n=='sqrt'):
    print((a**0.5),end=" ")
    print((b**0.5))
