from gpiozero import DigitalOutputDevice
import time
import argparse
from datetime import datetime
import logging


logging.getLogger().setLevel(logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("--PIN", type=int, default=17)
parser.add_argument("--ON_TIME", type=int, default=40)
args = parser.parse_args()

PUMP_PIN = args.PIN
ON_TIME = args.ON_TIME


def activate_pump(pump, on_time):
    try:
        logging.info("{} - pump on".format(datetime.now()))
        pump.on()
        time.sleep(on_time)
    except:
        pump.off()

    logging.info("{} - pump off".format(datetime.now()))
    pump.off()


pump = DigitalOutputDevice(f"GPIO{PUMP_PIN}", active_high=False)

# schedule.every(20).seconds.do(activate_pump, pump, ON_TIME)
logging.info("{} - Job started".format(datetime.now()))
activate_pump(pump, ON_TIME)
logging.info("{} - Job ended".format(datetime.now()))

# while True:
#     schedule.run_pending()
#     time.sleep(1)

