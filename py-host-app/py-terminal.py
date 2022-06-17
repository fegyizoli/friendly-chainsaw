# This python class should open a serial port to the arduino nano based keypad and print out
# everything that is received on that channel.

import serial

#Get the serial instance
serial_connection = serial.Serial()
serial_connection.baudrate = 9600
serial_connection.port = 'COM1'
serial_connection

#Open serial instance
serial_connection.open()
print ('serial is open? ', serial_connection.is_open ,'.\n')