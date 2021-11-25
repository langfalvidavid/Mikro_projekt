import RPi.GPIO as GPIO
import time, datetime

Szenzor = 40
Pumpa = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Szenzor, GPIO.IN)
GPIO.setup(Pumpa, GPIO.OUT)

def Működés(Szenzor):
  pontos_ido = datetime.datetime.now().strftime("%H:%M %Y-%m-%d")
  if GPIO.input(Szenzor):
    print("Száraz, vizet neki!")
    GPIO.output(Pumpa, GPIO.LOW)
  else:
    print("Megöntözve ekkor: ", pontos_ido)
    GPIO.output(Pumpa, GPIO.HIGH)
  
  while True:
    Működés(Szenzor)
    time.sleep(3)
