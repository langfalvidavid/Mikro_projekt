from RPi.GPIO import GPIO
import time

Szenzor = 40
Pumpa = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Szenzor, GPIO.OUT)
GPIO.setup(Pumpa, GPIO.IN)

def Működés:
  if (Szenzor):
    print("Száraz, vizet neki!")
    GPIO.output(Pumpa, GPIO.LOW)
  else:
    print("Megöntözve!")
    GPIO.output(Pumpa, GPIO.HIGH)
  
  while True:
    Működés(Szenzor)
    time.sleep(3)
