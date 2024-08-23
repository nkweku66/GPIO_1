from gpiozero import Buzzer, LED
from time import sleep

led = LED(17)
buzzer = Buzzer(2)

while True:
    buzzer.on()
    led.on()
    sleep(1)
    buzzer.off()
    led.off()
    sleep(1)
