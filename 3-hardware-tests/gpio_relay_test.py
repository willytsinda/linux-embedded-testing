import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
SOLAR_PIN = 23
BATTERY_PIN = 24

def test_switching():
    GPIO.setup(SOLAR_PIN, GPIO.OUT)
    GPIO.setup(BATTERY_PIN, GPIO.OUT)
    
    for _ in range(10):
        GPIO.output(SOLAR_PIN, GPIO.HIGH)
        GPIO.output(BATTERY_PIN, GPIO.LOW)
        time.sleep(5)
        
        GPIO.output(SOLAR_PIN, GPIO.LOW)
        GPIO.output(BATTERY_PIN, GPIO.HIGH)
        time.sleep(5)
