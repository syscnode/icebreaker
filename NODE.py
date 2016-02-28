# NODE
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.OUT)

ready_for_heartbreak = False

def  smile(channel):
    GPIO.output(6, GPIO.HIGH)
    print('thats the stuff')
    ready_for_heartbreak = True
    
GPIO.add_event_detect(26, GPIO.FALLING, callback=smile, bouncetime=200)

print('my heart..')

while(True):
    try:
        GPIO.wait_for_edge(19, GPIO.FALLING)
        GPIO.output(6, GPIO.LOW)
    except(KeyboardInterrupt):
        GPIO.cleanup()
