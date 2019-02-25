from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
matrixx = [[1.1],[1.1]]

add_edge(matrix,100,100,0,100,200,0)
add_edge(matrix,100,100,0,200,100,0)
add_edge(matrix,100,200,0,200,200,0)
add_edge(matrix,200,100,0,200,200,0)
draw_lines( matrix, screen, color )

for i in range(360):
    matrix_mult(matrixx,matrix)
    draw_lines(matrix,screen,color)
display(screen)
