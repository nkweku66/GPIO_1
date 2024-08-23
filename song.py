from gpiozero import PWMOutputDevice
from time import sleep

# Define the buzzer on GPIO pin 17
buzzer = PWMOutputDevice(2)

# Frequencies for musical notes (in Hz)
NOTES = {
    'C4': 261,
    'D4': 294,
    'E4': 329,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 493,
    'C5': 523
}

def play_tone(buzzer, frequency, duration):
    buzzer.frequency = frequency
    buzzer.value = 0.5  # 50% duty cycle
    sleep(duration)
    buzzer.value = 0

def play_song(buzzer):
    melody = [
        ('C4', 0.5),
        ('D4', 0.5),
        ('E4', 0.5),
        ('F4', 0.5),
        ('G4', 0.5),
        ('A4', 0.5),
        ('B4', 0.5),
        ('C5', 1.0)
    ]

    for note, duration in melody:
        play_tone(buzzer, NOTES[note], duration)

try:
    while True:
        play_song(buzzer)
        
except KeyboardInterrupt:
    buzzer.value = 0
