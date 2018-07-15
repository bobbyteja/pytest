#!/usr/bin/python
#This program will print the fibonacci series for a given input number.

a,b=0,1
x = int(input("Enter the input number:")) 
while b < x:
    print(b)
    a,b    = b,a+b
