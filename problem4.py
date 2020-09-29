#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:3
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"

L1=input('enter line 1: ')
L2=input('enter line 2: ')
L3=input('enter line 3: ')
L1=float(L1)
L2=float(L2)
L3=float(L3)
if L1 < L3 and L2 < L3:
    a=L1**2
    b=L2**2
    c=L3**2
elif L1 > L2 and L1 > L3:
    c=L1**2
    b=L2**2
    a=L3**2
elif L2 > L1 and L2 > L3:
    a=L1**2
    c=L2**2
    b=L3**2
elif L1 < L2 and L1 < L3:
    a=L3**2
    b=L2**2
    c=L1**2
elif L2 < L1 and L2 < L3:
    a=L3**2
    b=L1**2
    c=L2**2
elif L3 < L2 and L3 < L1:
    a=L3**2
    b=L1**2
    c=L3**2

if a+b >= c*0.98 and a+b <= c*1.02:
    print('that is a right triangle')
elif a+b > c*1.02:
    print('that is an acute triangle')
elif a+b < c*0.98:
    print('that is an obtuse triangle')

    
    