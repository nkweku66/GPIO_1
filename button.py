from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on

if button.when_pressed == True:
    print("Button pressed")
button.when_released = led.off

pause()