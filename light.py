import requests
import RPi.GPIO as GPIO

light_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(light_pin, GPIO.OUT)

r = requests.get('https://192.168.10.245:6969/api/User_/', verify=False)
print (r.status_code)
print (r.headers)
print (r.text[0:1000])

if r.status_code == 200:
        if  GPIO.input(light_pin):
                GPIO.output(light_pin, False)
        else:
                GPIO.output(light_pin, True)
else:
        print ("r.status_code != 200")
