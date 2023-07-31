# create a defining function to draw triangle lines

def draw_tri_angle(lines) :

    for i in range (1, lines + 1) :

        print(i * "* ")


number_of_lines =  int(input("Enter number of lines to draw a triangle : "))

draw_tri_angle(number_of_lines)