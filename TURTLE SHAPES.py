import turtle as t
tim =t.Turtle()


def draw_shapes(number_of_sides):
    angle= 360/number_of_sides
    

    for _ in range(number_of_sides):
       
        tim.forward(100)
        tim.right(angle)

for shape in range(3,11):
    draw_shapes(shape)
    
    