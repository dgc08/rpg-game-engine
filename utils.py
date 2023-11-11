from time import sleep

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

def printText(text):
    cuts = text.split(";")
    for i in cuts:
        if i.strip().startswith("Cut:"):
            sleep(float(i.replace("Cut:", "")))
            print()
        else:
            print(i.strip().replace("nwe", "\n"))
            getch()