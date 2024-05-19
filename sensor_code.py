# This is the code to run the MLX90614 Infrared Thermal Sensor
# You'll need to import the package "Adafruit Blinka"
# You'll need to import the package "adafruit-circuitpython-mlx90614/"
# You'll need to enable i2c on the pi https://pimylifeup.com/raspberry-pi-i2c/
# Reboot after enabling i2C
# Sensor is connected to 3.3V, GND and the i2C pins 3(SDA) and 5(SCL)

import board
import busio as io
import adafruit_mlx90614

from time import sleep

# i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
# mlx = adafruit_mlx90614.MLX90614(i2c)

# ambientTemp = "{:.2f}".format(mlx.ambient_temperature)
# targetTemp = "{:.2f}".format(mlx.object_temperature)

# sleep(1)

# print("Ambient Temperature:", ambientTemp, "°C")
# print("Target Temperature:", targetTemp,"°C")
#*********************************************************************************  
import random
import time
from queue import Queue


#create a queue to store random number

sensor_data_queue1 = Queue()
sensor_data_queue2 = Queue()

def generate_sensor_data():
    while True:
        i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
        mlx = adafruit_mlx90614.MLX90614(i2c)

        # ambientTemp = "{:.2f}".format(mlx.ambient_temperature)
        targetTemp = "{:.2f}".format(mlx.object_temperature)
        sensor_data_queue1.put((targetTemp, time.time()), timeout= 3)
        sensor_data_queue2.put((targetTemp, time.time()), timeout= 3)
        
        # print(sensor_data_queue.get(timeout= 3))
        # print(type(sensor_data_queue))
        # break

        time.sleep(1)

