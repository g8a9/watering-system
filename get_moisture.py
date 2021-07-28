import time
import schedule
from serial import Serial
from datetime import datetime

# calibrated
MIN_MOISTURE = 680  # air
MAX_MOISTURE = 360  # water
CONSUME_TIME = 10
SAMPLING_TIME = 60 * 20
LAST_READING = None


def dump_last_reading():
    with open("moisture.csv", "a") as fp:
        fp.write("{},{},{:.4f}\n".format(
            LAST_READING[0],
            LAST_READING[1],
            LAST_READING[2]
        ))


def read_soil_moisture(port):
    port.flush()
    if port.in_waiting > 0:
        moisture = port.readline().decode("utf-8").rstrip()
        moisture_bound = int(moisture)
        if moisture_bound < 360:
            moisture_bound = MAX_MOISTURE
        if moisture_bound > 680:
            moisture_bound = MIN_MOISTURE

        moisture_perc = \
            (moisture_bound - MAX_MOISTURE) / (MIN_MOISTURE - MAX_MOISTURE)
    else:
        print("No reading at ", datetime.now())
        return

    global LAST_READING
    LAST_READING = (datetime.now(), moisture, 1 - moisture_perc)
    print(datetime.now(), moisture, 1 - moisture_perc)


port = Serial("/dev/ttyACM0", 9600, timeout=1)
schedule.every(CONSUME_TIME).seconds.do(read_soil_moisture, port)
schedule.every(SAMPLING_TIME).seconds.do(dump_last_reading)

while True:
    schedule.run_pending()
    time.sleep(1)
