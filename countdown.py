import time
import pygame

pygame.mixer.init()


print("Hey guy!")
time.sleep(1)
print("So there's this cool thing in python")
time.sleep(2)
print("where you can mess with time")
time.sleep(1)
print("now i find this specially cool, something fun you can make is a countdown timer. ")
print("Like the type you use for pasta. ")

while True:
    countdown = input("Enter a time to countdown from (h:m:s): ")
    try:
        parts = countdown.split(":")
        if len(parts) != 3:
            raise ValueError("format")
        
        h, m, s = map(int, parts)
        if not (0 <= m < 60 and 0 <= s < 60):
            raise ValueError("range")
        
        break
    except ValueError as s:
        if str(s) == "format":
            print("That doesn't work, try doing it in h:m:s format (e.g. 06:06:06)")
        else:
            print("Woah, those numbers don't work for a timer man, you know how timers work right?")



def timer(countdown):
    parts = countdown.split(":")
    h = int(parts[0])
    m = int(parts[1])
    s = int(parts[2])

    total = h*3600 + m*60 + s
    for x in range(total, 0 , -1):
        seconds= x % 60
        minutes= int(x/60) % 60
        hours= int(x/3600) % 60
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep (1)

timer(countdown)
print("Time's up, your pasta is probably overcooked now.")
alarm_sound=pygame.mixer.Sound("Sounds/YOUR PHONE LINGING (sound effect).mp3")

alarm_sound.play()
time.sleep(5)