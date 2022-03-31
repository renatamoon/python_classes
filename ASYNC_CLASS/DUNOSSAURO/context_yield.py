from contextlib import contextmanager
from datetime import datetime
from time import time, sleep


@contextmanager
def time_counter(var):
    print('I just enter the context')
    t = datetime.now()
    yield var
    delta = datetime.now() - t
    print("I just leave the context")
    print("Total time in seconds: ", delta.seconds)


with time_counter('potato') as var:
    print('On the context', var)
    sleep(3)


