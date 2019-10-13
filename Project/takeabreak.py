import time
import webbrowser

break_time  = 3
break_count = 0

print("This program started on" + time.ctime())
while(break_count < break_time) :
    time.sleep(10)
    webbrowser.open("https://youtu.be/mx24IJTlffc")
    break_count += 1
