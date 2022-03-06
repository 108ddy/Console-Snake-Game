frame = width, height = 25, 10

def create_field(frame: tuple) -> list:
    for height in range(frame[1] + 2):
        for width in range(frame[0] + 2):
            if height == 0 or width == 0 or height == frame[1] + 1 or width == frame[0] + 1:
                print('#', end = '')
            else:
                print(' ', end = '')
        print()


def main():
    create_field(frame)


main()
