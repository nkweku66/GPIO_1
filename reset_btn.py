from gpiozero import LED, Button
from signal import pause
from subprocess import call



led = LED(17)
button = Button(2)

def print_thing():
    print ("button pressed")

button.when_pressed = print_thing

# button.when_pressed = led.on

# if button.when_pressed == True:
#     print("Button pressed")
# button.when_released = led.off

pause()