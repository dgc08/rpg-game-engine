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


class _Kbhit:
    def __init__(self):
        try:
            import msvcrt
            def kbhit():
                return msvcrt.kbhit()
        except ModuleNotFoundError:
            import sys
            import tty
            import termios
            import select

            def kbhit():
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(fd)
                    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
                        return True
                    else:
                        return False
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        self.impl = kbhit

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
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        return ch
    def decode(self, *args, **kwargs):
        return self.__call__()#.decode(*args, **kwargs)



class _GetchWindows:
    def __call__(self):
        try:
            import msvcrt
        except ModuleNotFoundError:
            return _GetchUnix()
        return msvcrt.getch()


getch = _Getch()
kbhit = _Kbhit()

def printText(text):
    cuts = text.split(";")
    for i in cuts:
        if i.strip().startswith("Cut:"):
            sleep(float(i.replace("Cut:", "")))
            print()
        else:
            print(i.strip().replace("nwe", "\n"))
            while not kbhit():
                pass
