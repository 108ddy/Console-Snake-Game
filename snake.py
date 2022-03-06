from time import sleep
from os import system
import keyboard
import platform
import random


frame = width, height = 25, 10
moving = 1


def clear():
    if platform.system() == 'Linux':
        return system('clear')
    else:
        return system('cls')


def food_spawn() -> None:
    food = [
        random.randrange(1, frame[0] + 1),
        random.randrange(1, frame[1] + 1),
    ]

    return food


def food_respawn() -> None:
    global apple_position, apple_spawn

    apple_position = food_spawn()
    apple_spawn = True


def initialize() -> None:
    global snake_head_position, direction, apple_spawn, apple_position

    snake_head_position = [frame[0] // 4, frame[1] // 2]
    direction = 'RIGHT'
    apple_spawn = True
    apple_position = food_spawn()

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
            elif apple_position[1] == height and apple_position[0] == width:
                char = '@'
            else:
                char = field[height][width]
            
            print(char, end = '')
        
        print()


def controls() -> None:
    global direction, apple_spawn

    if (keyboard.is_pressed('w') or keyboard.is_pressed('UP')) and direction != 'DOWN':
        direction = 'UP'
    elif (keyboard.is_pressed('d') or keyboard.is_pressed('RIGHT')) and direction != 'LEFT':
        direction = 'RIGHT'
    if (keyboard.is_pressed('s') or keyboard.is_pressed('DOWN')) and direction != 'UP':
        direction = 'DOWN'
    if (keyboard.is_pressed('a') or keyboard.is_pressed('LEFT')) and direction != 'RIGHT':
        direction = 'LEFT'

    moving_on_field(direction, apple_spawn, frame)


def moving_on_field(direction: str, apple_spawn: bool, frame_size: tuple) -> None:
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

    if apple_position[1] == snake_head_position[1] and apple_position[0] == snake_head_position[0]:
        apple_spawn = False
    
    if not apple_spawn:
        food_respawn()



def main():
    field = create_field(frame)

    while True:
        controls()
        draw_field(field, frame)
        sleep(.1)


main()
