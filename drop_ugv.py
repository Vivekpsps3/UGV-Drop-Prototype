from mavsdk import System, telemetry
import RPi.GPIO as GPIO
from time import sleep


def drop_ugv():
    UGV_pin = 12
    # Connect to the Pixhawk
    drone = System()
    drone.connect(system_address="udp://:14540")

    # Wait for the drone to connect
    while not drone.health_all_ok():
        print("Waiting for drone to connect...")
        sleep(1)

    # actuate servo
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(UGV_pin, GPIO.OUT)
    pwm = GPIO.PWM(UGV_pin, 50)
    pwm.start(7.5)


