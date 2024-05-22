import sensor_code

import time

while(True):
    new = sensor_code.sensor_data_queue1.get(timeout=3)
    print(new)