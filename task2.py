#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"

N=input("number=")
N=float(N)
if N > 0:
    print('positive')
if N == 0:
    print('zero')
if N < 0:
    print('negative')