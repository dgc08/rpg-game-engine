import msvcrt
import time
from random import randint

def count_spaces(input_string):
    # Find the position of '*' and '|'
    asterisk_position = input_string.find('*')
    pipe_position = input_string.find('#')

    # Check if both '*' and '|' are present and '*' comes before '|'
    if asterisk_position != -1 and pipe_position != -1:
        spaces_between = pipe_position - asterisk_position
        return abs(spaces_between)
    else:
        return 0


def get_input_with_timeout(timeout):
    start_time = time.time()
    while True:
        if msvcrt.kbhit():
            return True

        if time.time() - start_time >= timeout:
            return False


def update_text_in_place(text, screentime = 0.0001):
    print(text, end='', flush=True)
    time.sleep(screentime)  # You can adjust the delay as needed
    print('\r' + ' ' * len(text) + '\r', end='', flush=True)

def attack():
    base = ' ' * 100
    winpos = randint(1, 100)
    base = base[:winpos - 1] + '#' + base[winpos:]
    update_text_in_place(base, 1)

    for i in range(1,100):
        base = base[:i - 1] + '*' + base[i:]

        print(base, end='', flush=True)
        if get_input_with_timeout(0.025):
            return count_spaces(base)
            break
        print('\r' + ' ' * len(base) + '\r', end='', flush=True)

        if i != winpos:
            base = base[:i - 1] + ' ' + base[i:]
        else:
            base = base[:i - 1] + '#' + base[i:]
    for i in range(100,0, -1):
        base = base[:i - 1] + '*' + base[i:]

        print(base, end='', flush=True)
        if get_input_with_timeout(0.02):
            return count_spaces(base) * 2
            break
        print('\r' + ' ' * len(base) + '\r', end='', flush=True)

        if i != winpos:
            base = base[:i - 1] + ' ' + base[i:]
        else:
            base = base[:i - 1] + '#' + base[i:]

    return 200
