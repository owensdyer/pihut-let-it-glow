from machine import Pin
import time


def activity_one(duration):
    """
    Turn on block LED
    
    :param duration: The duration of time the block LED is on for in seconds.
    """
    block_led = Pin(14, Pin.OUT)
    block_led.value(1)

    print("Block LED on!")

    time.sleep(duration)

    # Turn light off
    block_led.value(0)


def activity_two(duration):
    """
    Turn on block LED and pico LED.
    
    :param duration: The duration of time the block and pico LEDs are on for in seconds.
    """
    pico_led = Pin(25, Pin.OUT)
    pico_led.value(1)

    block_led = Pin(14, Pin.OUT)
    block_led.value(1)

    print("Block and board LED on!")

    time.sleep(duration)

    # Turn lights off
    pico_led.value(0)
    block_led.value(0)


def activity_three(duration, cycle):
    """
    Flash the block LED.
    
    :param duration: The duration of time the lights are on and off for in seconds.
    :param cycle: The number cycles the lights flash for.
    """
    block_led = Pin(14, Pin.OUT)

    i = 0
    while i < cycle:
        block_led.value(1)
        time.sleep(duration)
        block_led.value(0)
        time.sleep(duration)
        i += 1

def run():
    activity_one(2)
    time.sleep(1)
    activity_two(2)
    time.sleep(1)
    activity_three(0.2, 10)

run()
