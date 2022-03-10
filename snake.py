from time import sleep
from os import system
from sys import exit
import keyboard
import platform
import random


class Field(object):
    def __init__(self, frame) -> None:
        self.frame = frame
        self.field = self.create_field()
        self.snake_position = [
            [self.frame[0] // 4, self.frame[1] // 2],
        ]
        self.apple_position = self.food_spawn()
        self.score = 0


    def create_field(self) -> list:
        field = [[]]

        for height in range(self.frame[1] + 2):
            field.append([])

            for width in range(self.frame[0] + 2):
                if height == 0 or width == 0 or height == self.frame[1] + 1 or width == self.frame[0] + 1:
                    self.char = '#'
                else:
                    self.char = ' '

                field[height].append(self.char)

        return field


    def draw_field(self) -> None:
        self.clear()

        for height in range(self.frame[1] + 2):
            for width in range(self.frame[0] + 2):
                if self.snake_position == [width, height]:
                    self.char = '◆'
                elif self.apple_position == [width, height]:
                    self.char = '@'
                else:
                    is_tail = False

                    for tail in self.snake_position:
                        if tail == [width, height]:
                            self.char = '◆'
                            is_tail = True

                    if not is_tail:
                        self.char = self.field[height][width]

                print(self.char, end = '')

            print()

        self.draw_score()


    def food_spawn(self) -> list:
        return [
            random.randrange(1, self.frame[0] + 1),
            random.randrange(1, self.frame[1] + 1),
        ]


    def clear(self) -> int:
        return system('clear') if platform.system() == 'Linux' else system('cls')


    def draw_score(self) -> None:
        print('=' * (self.frame[0] + 2))
        print(f'# Score: {self.score:{self.frame[0] - 9}} #')
        print('=' * (self.frame[0] + 2))


class Snake(object):
    def __init__(self, field: Field) -> None:
        self.field = field
        self.apple_spawn = True
        self.direction = 'RIGHT'

    def controls(self) -> None:
        if (keyboard.is_pressed('w') or keyboard.is_pressed('UP')) and self.direction != 'DOWN':
            self.direction = 'UP'
        elif (keyboard.is_pressed('d') or keyboard.is_pressed('RIGHT')) and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        elif (keyboard.is_pressed('s') or keyboard.is_pressed('DOWN')) and self.direction != 'UP':
            self.direction = 'DOWN'
        elif (keyboard.is_pressed('a') or keyboard.is_pressed('LEFT')) and self.direction != 'RIGHT':
            self.direction = 'LEFT'

        self.moving_on_field()
    

    def moving_on_field(self) -> None:
        self.snake_head = self.field.snake_position[-1][:]

        if self.direction == 'UP':
            self.snake_head[1] -= 1
        elif self.direction == 'RIGHT':
            self.snake_head[0] += 1
        elif self.direction == 'DOWN':
            self.snake_head[1] += 1
        elif self.direction == 'LEFT':
            self.snake_head[0] -= 1

        self.snake_head = self.field_limit(self.snake_head)
        del(self.field.snake_position[0])
        self.field.snake_position.append(self.snake_head)

        if self.field.apple_position == self.snake_head:
            self.apple_spawn = False
            self.field.score += 1
            self.snake_increase()

        if not self.apple_spawn:
            self.food_respawn()


    def field_limit(self, position: list) -> list:
        if position[1] < 1:
            position[1] = self.field.frame[1]
        elif position[0] > self.field.frame[0]:
            position[0] = 1
        elif position[1] > self.field.frame[1]:
            position[1] = 1
        elif position[0] < 1:
            position[0] = self.field.frame[0]

        return position

    def snake_increase(self) -> None:
        tail = self.snake_head[:]

        if len(self.field.snake_position) > 1:
            prev, next_prev = self.field.snake_position[0], self.field.snake_position[1]
            tail = prev[:]

            if prev[1] < next_prev[1]:
                tail[1] -= 1
            elif prev[0] > next_prev[0]:
                tail[0] += 1
            elif prev[1] > next_prev[1]:
                tail[1] += 1
            elif prev[0] < next_prev[0]:
                tail[0] -= 1

        tail = self.field_limit(tail)
        self.field.snake_position.insert(0, tail)


    def food_respawn(self) -> None:
        while self.field.apple_position in self.field.snake_position:
            self.field.apple_position = self.field.food_spawn()

        self.apple_spawn = True


    def game_over(self) -> bool:
        return (
            self.snake_head in self.field.snake_position[:-3] or keyboard.is_pressed('Esc') or self.field.score > 9999999999999999
        )


def main():
    frame = 25, 10
    field = Field(frame)
    snake = Snake(field)

    try:
        while True:
            snake.controls()
            field.draw_field()
            sleep(.2)

            if snake.game_over():
                exit()
    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    main()
