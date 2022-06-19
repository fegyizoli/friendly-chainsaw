# This python class should open a serial port to the arduino nano based keypad and print out
# everything that is received on that channel.
import serial
import serial.tools.list_ports

BAUDRATE = 9600

#returns back with available comport list
def get_comports():
    return serial.tools.list_ports.comports(include_links=False)

#opening first available comport and returns true if its possible
#else returns false
def open_comport():
    comport_list = get_comports()
    for connectable_port in comport_list:
        try:
            s = serial.Serial(connectable_port.name)
            s.baudrate = BAUDRATE
            print("Try to connect to "+connectable_port.name+".\n")
            s.close() #todo: temporarly solves the opened port issue
            s.open()
        except (OSError, serial.SerialException) as e:
            print("Cannot connect to "+connectable_port.name+".\n")
            print(e)
            s.close()
            retval = False
        else:
            print("Connected successfully to "+connectable_port.name+".\n")
            retval = True
            break
    if retval == True:
        barray = bytearray(10)
        s.readinto(barray)
        s.close()
        print(barray)
    return retval
    
    
#Open serial instance
#serial_connection = serial.Serial()
#start_serial_communication(serial_connection, 9600)
if open_comport() == True :
    print("Yes.\n")
else:
    print("No.\n")
