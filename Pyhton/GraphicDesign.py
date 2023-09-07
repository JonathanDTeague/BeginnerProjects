def draw_triangle(base, character):
    if base % 2 == 0:
        base += 1  
    for i in range(1, base + 1, 2):
        line = (character * i).center(base, ' ')
        print(line)
    count = (base + 1) / 2
    print(count)

draw_triangle(6,"X")