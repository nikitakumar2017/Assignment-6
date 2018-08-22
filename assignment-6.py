#Q.1- Create a function to calculate the area of a sphere by taking radius from user.
import math
def area(r):
    area=(4*math.pi*(r**2))
    return area
r=int(input("Enter radius "))
print("Area of sphere is ",area(r))


#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number.
#Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number.
#E.g., 6 is a perfect number because 6=1+2+3].
def perfect(num):
    i=1
    sumoffact=0
    while(i<num):
        if(num%i==0):
            sumoffact=sumoffact+i
        i+=1
    if(sumoffact==num):
        return 0
    else:
        return 1

j=1
ans=0
print("Perfect numbers between 1 and 1000 are: ",end=' ')
while(j<1000):
    ans=perfect(j)
    if(ans==0):
        print(j,end=' ')
        
    j+=1 

#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
def table(num):
    i=1
    while(i<=10):
        print(num,'x',i,'=',num*i)
        i+=1

n=int(input("Enter number whose table you want "))
table(n)

#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(a,b):
    if(b==0):
        return 1
    elif(b>1):
        return a*power(a,b-1)
    else:
        return a

a=int(input("Enter number 1 "))
b=int(input("Enter number 2 "))
ans=power(a,b)
print("a^b = ",ans)
