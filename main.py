from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
matrixx = [[1.1,0,0,0],
           [0,1.1,0,0],
           [0,0,1.1,0],
           [0,0,0,1.1]]

add_edge(matrix,100,100,0,100,200,0)
add_edge(matrix,100,100,0,200,100,0)
add_edge(matrix,100,200,0,200,200,0)
add_edge(matrix,200,100,0,200,200,0)
draw_lines( matrix, screen, color )

def r(a):
    c = 0
    while c < len(a):
        counter = 0
        while counter < len(a[0]):
            a[c][counter] = round(a[c][counter])
            counter += 1
        c += 1

for i in range(50):
    #print("matrix before: \n")
    #print_matrix(matrix)
    matrix_mult(matrixx,matrix)
    
    print_matrix(matrix)
    r(matrix)
    print_matrix(matrix)
    
    #print("matrix after: \n")
    #print_matrix(matrix)
    draw_lines(matrix,screen,color)

display(screen)
