#!/usr/bin/env python

"""
vom scrie un executabil care primește în linie de comandă
un timestamp la care să execute o notificare.


timestamp-ul va fi primit în unul din formatele:

11:22:33
11:22
11


"""
import datetime
from time import sleep
import sys
from os import path


# task 1: parsăm timestamp din string
#         în obiect intern
def parse_timespec(ts):
    """
    receives a timespec of the form
    11:22:33 # or
    11:22    # or
    11

    and returns a datetime.time object
    """
    parts = ts.split(":")
 
    return datetime.time(*[
        int(item) for item in parts
    ])

# task 2: să aflăm cât trebuie să așteptăm
#         până rulăm payload-ul (notificarea)
def get_time_until(tspec):
    """
    receives a datetime.time object
    and calculates the seconds that will pass
    until that time is reached
    """

    today = datetime.date.today()
    now = datetime.datetime.now()
    tspec

    when = datetime.datetime.combine(today, tspec)

    if when < now:
        when = now + datetime.timedelta(days=1)

    diff = when - now

    return diff.total_seconds()


# task 3: să aștepăm diferența de timp rezultată
#         și să executăm

def schedule(func, wait):
    """
    waits `wait` seconds
    and executes `func`
    """
    sleep(wait)
    func()


def notify():
    print("A L E R T   A L E R T   A L E R T")


# task 4: să îl facem executabil de sistem
if __name__ == "__main__":
    try:
        ts = sys.argv[1]
    except IndexError:
        fname = path.basename(sys.argv[0])
        print(f"Usage: {fname} <timespec>" )
    else:
        seconds = get_time_until(parse_timespec(ts))
        schedule(notify, seconds)