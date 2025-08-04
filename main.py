from machine import Pin
from utime import sleep

print ('Hello World!')

red = Pin(15, Pin.OUT)
yellow = Pin(16, Pin.OUT)
green = Pin(18, Pin.OUT)

while True:
    
    red.on()
    print("Vermelho ON! Ligado")
    sleep(7.0)
    red.off()
    print("Vermelho OFF! Desligado")
    sleep(0.5)

    yellow.on()
    print("Amarelo ON! Ligado")
    sleep(10.0)
    yellow.off()
    print("Amarelo OFF! Desligado")
    sleep(0.5)

    green.on()
    print("Verde ON! Ligado")
    sleep(20.0)
    green.off()
    print("Verde OFF! Desligado")
    sleep(0.5)
    
    
    