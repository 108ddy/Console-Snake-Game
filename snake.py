from time import sleep
from os import system
import keyboard
import platform


frame = width, height = 25, 10
moving = 1


def clear():
    if platform.system() == 'Linux':
        return system('clear')
    else:
        return system('cls')


def initialize() -> None:
    global snake_head_position, direction

    snake_head_position = [frame[0] // 4, frame[1] // 2]
    direction = 'RIGHT'


initialize()


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
    clear()
    
    for height in range(frame[1] + 2):
        for width in range(frame[0] + 2):
            if (snake_head_position[1] == height and snake_head_position[0] == width and
                snake_head_position[1] != 0 and snake_head_position[0] != 0 and
                snake_head_position[1] != frame[1] + 2 and snake_head_position[0] != frame[0] + 2):
                char = '■'
            else:
                char = field[height][width]
            
            print(char, end = '')
        
        print()


def controls() -> None:
    global direction

    if (keyboard.is_pressed('w') or keyboard.is_pressed('UP')) and direction != 'DOWN':
        direction = 'UP'
    elif (keyboard.is_pressed('d') or keyboard.is_pressed('RIGHT')) and direction != 'LEFT':
        direction = 'RIGHT'
    if (keyboard.is_pressed('s') or keyboard.is_pressed('DOWN')) and direction != 'UP':
        direction = 'DOWN'
    if (keyboard.is_pressed('a') or keyboard.is_pressed('LEFT')) and direction != 'RIGHT':
        direction = 'LEFT'

    moving_on_field(direction, frame)


def moving_on_field(direction: str, frame_size: tuple) -> None:
    if direction == 'UP':
        snake_head_position[1] -= moving
    elif direction == 'RIGHT':
        snake_head_position[0] += moving
    elif direction == 'DOWN':
        snake_head_position[1] += moving
    elif direction == 'LEFT':
        snake_head_position[0] -= moving

    if snake_head_position[1] < 0:
        snake_head_position[1] = frame_size[1]
    elif snake_head_position[0] > frame_size[0]:
        snake_head_position[0] = 0
    elif snake_head_position[1] > frame_size[1]:
        snake_head_position[1] = 0
    elif snake_head_position[0] < 0:
        snake_head_position[0] = frame_size[0]


def main():
    field = create_field(frame)

    while True:
        controls()
        draw_field(field, frame)
        sleep(.1)


main()
