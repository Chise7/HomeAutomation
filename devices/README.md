This folder will be a collection of the code written for the individual microcontrollers and system devices.

ESP32C6:

This device takes a bit of configuration to initially setup. I followed this guide, and keep copies of my code in this repository.
https://wiki.seeedstudio.com/xiao_esp32c6_micropython/

Laundry: 
Utilize ESP32 device to send a wifi request to backend which will trigger a text message to my phone, telling me when laundry is started and done. 
This will be sensed by an SW-420 with the following soldered pin connections:
V_d -> 3v3
GND -> GND
Data -> GPIOXX
Code will be written in MicroPython.

Raspberry Pi Zero:
Utilize DHT22 sensor to detect temperature and moisture, and wirelessly send data back to database.
Pin Connections:
V_d -> 3v3
GND -> GND
Data -> GPIOXX
Initial code will be written in micropython, however there are plans for a future Rust version.