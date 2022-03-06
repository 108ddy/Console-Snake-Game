frame = width, height = 25, 10
snake_head_position = [frame[0] // 4, frame[1] // 2]


def create_field(frame: tuple) -> list:
    field = [[]]
    
    for height in range(frame[1] + 2):
        field.append([])
        
        for width in range(frame[0] + 2):
            if height == 0 or width == 0 or height == frame[1] + 1 or width == frame[0] + 1:
                char = '#'
            else:
                char = ' '

            field[height].append(char)

    return field


def draw_field(field: list, frame: tuple) -> None:
    for height in range(frame[1] + 2):
        for width in range(frame[0] + 2):
            if snake_head_position[1] == height and snake_head_position[0] == width:
                char = '@'
            else:
                char = field[height][width]
            
            print(char, end = '')
        
        print()


def main():
    field = create_field(frame)

    draw_field(field, frame)


main()
