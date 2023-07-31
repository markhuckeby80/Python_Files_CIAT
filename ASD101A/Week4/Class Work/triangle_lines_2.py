# create a defining function to draw triangle lines with an outer and inner loop

def draw_tri_angle(lines) :

    for i in range (1, lines + 1):
        for j in range (1, i + 1):
            print("*", end=" ")
        
        print()


number_of_lines =  int(input("Enter number of lines to draw a triangle : "))

draw_tri_angle(number_of_lines)