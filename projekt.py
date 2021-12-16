import RPi.GPIO as GPIO
import time, datetime
from pushbullet import Pushbullet

GPIO.setwarnings(False)

pb = Pushbullet("o.MA0CxmOB3mb4DL0Yp7WLHPpDSqp69fLM")
print(pb.devices)
Szenzor = 40
Pumpa = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Szenzor, GPIO.IN)
GPIO.setup(Pumpa, GPIO.OUT)


while True:
    pontos_ido=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if GPIO.input(Szenzor):
        GPIO.output(Pumpa, GPIO.LOW)
        time.sleep(2)
    else:
        GPIO.output(Pumpa, GPIO.HIGH)
        time.sleep(2)
        dev=pb.get_device('Xiaomi Mi 9 SE')
        push=dev.push_note("Megöntözve ekkor:", pontos_ido)
    
