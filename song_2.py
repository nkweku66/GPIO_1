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
    'C5': 523,
    'D5': 587,
    'E5': 659,
    'F5': 698,
    'G5': 784,
    'A5': 880,
    'B5': 987,
    'C6': 1047
}

# Define the melody and rhythm (note, duration in seconds)
melody = [
    ('E5', 0.5), ('E5', 0.5), ('E5', 0.5), ('E5', 0.5), ('E5', 0.5), ('E5', 0.5),
    ('E5', 1.0), ('G5', 0.5), ('E5', 0.5), ('A5', 1.0), ('A5', 0.5), ('A5', 0.5),
    ('A5', 1.0), ('G5', 0.5), ('E5', 0.5), ('C5', 1.0), ('C5', 0.5), ('C5', 0.5),
    ('C5', 1.0), ('C5', 0.5), ('E5', 0.5), ('E5', 1.0), ('E5', 0.5), ('E5', 0.5),
    ('E5', 0.5), ('E5', 0.5), ('E5', 1.0), ('G5', 0.5), ('E5', 0.5), ('A5', 1.0),
    ('A5', 0.5), ('A5', 0.5), ('A5', 1.0), ('G5', 0.5), ('E5', 0.5), ('C5', 1.0),
]

def play_tone(buzzer, frequency, duration):
    if frequency > 0:
        buzzer.frequency = frequency
        buzzer.value = 0.5  # 50% duty cycle
    else:
        buzzer.value = 0
    sleep(duration)
    buzzer.value = 0

try:
    while True:
        for note, duration in melody:
            play_tone(buzzer, NOTES[note], duration)
except KeyboardInterrupt:
    buzzer.value = 0
