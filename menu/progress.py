import sys
import time


def spinning_cursor():
    while 1:
        for cursor in '|/-\\':
            yield cursor


def spinner_task(ctx, newline=True):
    delay = 0.1
    spinner = spinning_cursor()
    while ctx.busy:
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\b')
        sys.stdout.flush()
    if newline:
        sys.stdout.write('\n')
    sys.stdout.flush()
