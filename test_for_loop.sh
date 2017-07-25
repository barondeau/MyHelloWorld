#!/bin/bash
# Assign variable y to 0
y=0

#repeat outer loop 3 times
for y in 1 2 3
do
#repeat inner loop 3 times
    for x in "Monday" "Tuesday" "Wednesday"
    do
#print x
        echo $x
     done
#print blank line
     echo " "
done
