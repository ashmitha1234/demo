# demo
def ispalindrome(x): 
    a=x
    rev = 0
    while x>0:
        n = x % 10 #1
        rev = rev * 10 + n
        x //= 10    
    if rev==a:
       print("It is a palindrome")
    else:
       print("It is a not a palindrome")

x=int(input("Enter a number : "))
ispalindrome(x)
