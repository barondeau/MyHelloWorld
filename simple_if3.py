#!/usr/bin/env python
x =0
y=70
counter=0
b = True
c=1
while b == True:
    if b==True:
        x=raw_input("Enter a number ")
        counter=counter+c
    if int(x)>int(y):
        print "Your guess is too high "
    elif int(x)<int(y):
        print "Your guess is too low"
    else:
        print "You got the number ", y
        print "It took you ", counter, "many guesses"
        b=False
        
    
