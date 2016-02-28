# NODE
import RPi.GPIO as GPIO
from Adafruit_PWM_Servo_Driver import PWM
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pwm = PWM(0x40)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.OUT)

ready_for_heartbreak = False

servoMin = 150
servoMax = 600

def setServoPulse(channel, pulse):
    pulseLength = 1000000
    pulseLength /= 60
    pulseLength /= 4096
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)

def smile(channel):
    GPIO.output(6, GPIO.HIGH)
    print('thats the stuff')
    ready_for_heartbreak = True
    
GPIO.add_event_detect(26, GPIO.FALLING, callback=smile, bouncetime=200)

print('my heart..')



while(True):
    pwm.setPWM(0, 0, servoMin)
    time.sleep(1)
    pwm.setPWM(0, 0, servoMax)
    time.sleep(1)
    
    try:
        GPIO.wait_for_edge(19, GPIO.FALLING)
        GPIO.output(6, GPIO.LOW)
    except(KeyboardInterrupt):
        GPIO.cleanup()
