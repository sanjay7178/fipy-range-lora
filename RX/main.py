# # ---------------------------------------------------
# # tx messages with lora-mac
# # see:
# # loramac
# # https://docs.pycom.io/pycom_esp32/pycom_esp32/tutorial/includes/lora-mac.html
# # https://forum.pycom.io/topic/934/lora-stats-documentation-is-missing-the-parameter-must-passed/2

# import network
# from network import LoRa
# import binascii
# import socket
# import machine
# import time
# import binascii
# import sys
# import utils # utilities module with CRC calculation
# import pycom

# # Initialize LoRa in LORA mode.
# lora = LoRa(mode=LoRa.LORA, tx_power=5, region=LoRa.EU868, frequency=865062500)

# # Use frequencies for Nepal
# lora.remove_channel(1)
# lora.remove_channel(2)
# lora.remove_channel(3)

# pycom.heartbeat(False)

# print ("Waiting for packets...")

# # tx loop
# while True:
#     s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
#     s.setblocking(False)
#     # receive up to 256 characters
#     dataRx = s.recv(256)
#     print (dataRx)
#     # get lora stats (data is tuple)
#     LoraStats = lora.stats()
#     print(LoraStats)

#     pycom.rgbled(0x7f7f00) # yellow
#     time.sleep(2)



# from machine import Pin, I2C
# import ssd1306

# i2c = I2C(1, pins=('P9', 'P10')) #For ESP32: pin initializing

# oled_width = 128
# oled_height = 64
# oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
# # Clear the display
# oled.fill(0)
# oled.show()

# # Draw some text
# oled.text("Hello, world!", 0, 0)
# oled.text("This is an", 0, 16)
# oled.text("OLED display", 0, 32)
# oled.show()


import network
from network import LoRa
import binascii
import socket
import machine
import time
import binascii
import sys
import utils  # utilities module with CRC calculation
import pycom
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Initialize LoRa in LORA mode.
lora = LoRa(mode=LoRa.LORA, tx_power=5, region=LoRa.EU868, frequency=865062500)

# Use frequencies for Nepal
lora.remove_channel(1)
lora.remove_channel(2)
lora.remove_channel(3)

pycom.heartbeat(False)

# Initialize the I2C interface for the SSD1306 display
i2c = I2C(0, pins=("P9", "P10"))  # SDA, SCL
display = SSD1306_I2C(128, 64, i2c)

print("Waiting for packets...")

# tx loop
while True:
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setblocking(False)
    # receive up to 256 characters
    dataRx = s.recv(256)
    print(dataRx)

    # Get LoRa stats
    lora_stats = lora.stats()
    rssi = lora_stats[1]
    snr = lora_stats[2]
    sfrx = lora_stats[3]
    sftx = lora_stats[4]
    tx_trials = lora_stats[5]
    tx_time_on_air = lora_stats[7]
    tx_counter = lora_stats[8]
    tx_frequency = lora_stats[9]

    # Display information on the SSD1306 display
    display.fill(0)  # Clear the display
    display.text("RSSI: {}".format(rssi), 0, 0)
    display.text("SNR: {}".format(snr), 0, 10)
    display.text("SFRX: {}".format(sfrx), 0, 20)
    display.text("SFTX: {}".format(sftx), 0, 30)
    display.text("TX Trials: {}".format(tx_trials), 0, 40)
    display.text("TX Time: {}".format(tx_time_on_air), 0, 50)
    display.show()

    pycom.rgbled(0x7f7f00)  # yellow
    time.sleep(2)
