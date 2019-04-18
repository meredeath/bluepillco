"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    final = ""
    for i in matrix:
        for j in i:
            final += str(j)
            final += " "
        final += "\n"
    print(final)

#print_matrix([[0,1,2,3],[0,1,2,3],[0,1,2,3]])

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    counter = 0
    length = len(matrix)
    while counter < length:
        for i in range(length):
            if i == counter:
                matrix[counter][i] = 1
            else:
                matrix[counter][i] = 0
        counter += 1
    return

#few tests I'm just going to comment out
m1 = [[0,1,2,3],[0,1,2,3],[0,1,2,3],[2,7,4,8]]
#ident(m1)
m2 = [[3,4,5,6],[2,4,8,6],[35,87,9,5],[34,7,53,8]]

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #columns of first equals rows of second
    #for each row in the first matrix, we're going to take the dot product
    m1row = 0
    m2col = 0
    lim = len(m1)
    ans = []
    for i in range(lim):
        ans.append([])
    for i in ans:
        c = 0
        while c < lim:
            i.append(0)
            c += 1
    while m1row < lim:
        m2col = 0
        while m2col < lim:
            s = 0
            counter = 0
            while counter < lim: #sums the dot product             
                s += m1[m1row][counter] * m2[counter][m2col]
                counter += 1
            ans[m1row][m2col] = s
            m2col += 1
        m1row += 1
            
    a = 0
    b = 0
    while a < len(ans):
        b = 0
        while b < len(ans[0]):
            m2[a][b] = ans[a][b]
            b += 1
        a += 1
            

print("before: \n")
print_matrix(m1)
print_matrix(m2)
matrix_mult(m1,m2)
print("\nafter\n")
print_matrix(m2)
        
def new_matrix(rows = 4, cols = 4):
    m = []
    '''
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    '''
    return m
