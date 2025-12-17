from machine import Pin

board_led = Pin(25, Pin.OUT)
board_led.value(1)

print("Light on")
