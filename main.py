# 9AM-5PM = 8 hours = 480 min
from pygame import mixer
import time

# since we have to drink 3.5 litres of water between 9-5
mixer.init()
watertimedelay = round((480*200)/(3.5*1000))
print(watertimedelay) # After 27 min each time water.mp3 will play

eyetimedelay = 30 # After each 30 min eye.mp3 will play
physictimedelay = 45 # After each 45 min physic.mp3 will play

count=0
while(count<480):
    time.sleep(60)
    count+=1

    if count%watertimedelay==0:
        mixer.music.load("water.mp3")
        mixer.music.play()
        query = input()
        if query=="drink":
            mixer.music.stop()

    if count%eyetimedelay==0:
        mixer.music.load("eye.mp3")
        mixer.music.play()
        query = input()
        if query=="eydone":
            mixer.music.stop()

    if count%physictimedelay==0:
        mixer.music.load("physic.mp3")
        mixer.music.play()
        query = input()
        if query=="exdone":
            mixer.music.stop()
