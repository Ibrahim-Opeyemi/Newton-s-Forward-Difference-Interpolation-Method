# Method 1: By prompting the user to input the values for x and y flexibly;

"""
Created on Mon Oct 25 09:21:09 2021

@author: OPEYEMI IBRAHIM
"""
# Python 3 Program to Interpolate Using Newton Forward Difference Interpolation

# Method 1: By prompting the user to input the values for x and y flexibly;

# Importing NumPy Library
import numpy as np

def u_cal(u, n):

    temp = u;
    for i in range(1, n):
        temp = temp * (u - i);
    return temp;

# calculating factorial of given number n
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;

# Reading number of unknowns
n = int(input('Enter number of data points: '))

# Making numpy array of n & n x n size and initializing
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n,n))

# Reading data points
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i][0] = float(input( 'y['+str(i)+']='))

# Generating forward difference table
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]

print ('\nOUTPUT RESULT:\n')

print('\nFORWARD DIFFERENCE TABLE\n');

for i in range(n):
    print('%0.2f' %(x[i]), end='')
    for j in range(1, n):
        print('\t\t%0.2f' %(y[i][j]), end='')
    print()

# Value to interpolate at
value = 1.5;

# initializing u and sum
sum = y[0][0];
u = (value - x[0]) / (x[1] - x[0]);
for i in range(1,n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i);

print("\nValue at", value, "is", round(sum, 6));


# print a line '-' 50 times after running codes for Method 1: By prompting the user to input the values for x and y flexibly;
print('-'*50)

#--------------------------------------------------#