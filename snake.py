from time import sleep
from os import system
import keyboard
import platform
import random


frame = width, height = 25, 10
moving = 1
score = 0


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
    global snake_position, snake_head, direction, apple_spawn, apple_position
    
    snake_position = [
        [frame[0] // 4, frame[1] // 2],
    ]
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
            if snake_head == [width, height]:
                char = '◆'
            elif apple_position == [width, height] and apple_position not in snake_position:
                char = '@'
            else:
                prints = False

                for tail in snake_position:
                    if tail == [width, height]:
                        char = '◆'
                        prints = True
                
                if not prints: 
                    char = field[height][width]
            
            print(char, end = '')
        
        print()
    
    print(f'Score: {score}')


def snake_increase() -> None:
    tail = snake_head[:]

    if len(snake_position) > 1:
        a, b = snake_position[0], snake_position[1]
        tail = a[:]
    
        if a[1] < b[1]:
            tail[1] -= 1
        elif a[0] > b[0]:
            tail[0] += 1
        elif a[1] > b[1]:
            tail[1] += 1
        elif a[0] < b[0]:
            tail[0] -= 1

    tail = field_limit(tail, frame)
    snake_position.insert(0, tail)


def controls() -> None:
    global direction 
    
    if (keyboard.is_pressed('w') or keyboard.is_pressed('UP')) and direction != 'DOWN':
        direction = 'UP'
    elif (keyboard.is_pressed('d') or keyboard.is_pressed('RIGHT')) and direction != 'LEFT':
        direction = 'RIGHT'
    elif (keyboard.is_pressed('s') or keyboard.is_pressed('DOWN')) and direction != 'UP':
        direction = 'DOWN'
    elif (keyboard.is_pressed('a') or keyboard.is_pressed('LEFT')) and direction != 'RIGHT':
        direction = 'LEFT'

    moving_on_field(direction, frame)


def field_limit(position: list, frame_size: tuple) -> list:
    if position[1] < 1:
        position[1] = frame_size[1]
    elif position[0] > frame_size[0]:
        position[0] = 1
    elif position[1] > frame_size[1]:
        position[1] = 1
    elif position[0] < 1:
        position[0] = frame_size[0]

    return position


def moving_on_field(direction: str, frame_size: tuple) -> None:
    global snake_head, snake_position, apple_spawn, score
     
    snake_head = snake_position[-1][:]

    if direction == 'UP':
        snake_head[1] -= moving
    elif direction == 'RIGHT':
        snake_head[0] += moving
    elif direction == 'DOWN':
        snake_head[1] += moving
    elif direction == 'LEFT':
        snake_head[0] -= moving

    snake_head = field_limit(snake_head, frame_size)
    del(snake_position[0])
    snake_position.append(snake_head)

    if apple_position == snake_head:
        apple_spawn = False
        score += 1
        snake_increase()

    if not apple_spawn:
        food_respawn()


def main():
    field = create_field(frame)

    while True:
        controls()
        draw_field(field, frame)
        sleep(.2)


main()
