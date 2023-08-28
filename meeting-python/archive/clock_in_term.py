from time import strftime, sleep, asctime
from re import match, search

while 1:
    cur_time = search(r'\d\d:\d\d:\d\d', asctime())
    print(cur_time.group(0), end='')
    sleep(1)
    print("\u001b[A2")
