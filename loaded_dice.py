from microbit import *
import random

dice = [
    Image("90009:00000:90009:00000:90009"),
    Image("90009:00000:00900:00000:90009"),
    Image("90009:00000:00000:00000:90009"),
    Image("00009:00000:00900:00000:90000"),
    Image("00009:00000:00000:00000:90000"),
    Image("00000:00000:00900:00000:00000")
    ];

display.show(random.choice(dice));

while True:
    if accelerometer.is_gesture("shake"):
        # roll animation
        display.clear();
        while accelerometer.is_gesture("shake"):
            pass;
        if accelerometer.get_x() > 40:
            display.show(dice[0]);
        else:
            display.show(random.choice(dice));
