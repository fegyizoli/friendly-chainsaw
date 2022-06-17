# friendly-chainsaw
This is basically a macro keypad project with some differences:
- the keys attached to different clipboards
- there will be a PC app (written in Python) that managing the clipboards and the assignment of the keys

A macro keypad but not in the easiest way possible: it is based on an Arduino Nano (ATmega 328P).
I also have a 4x4 matrix keypad that is good for this project.

### Why: 
- because I had a Nano that is only takes up space in my drawer.
- Want some challenge since the world is already full with arduino projects.
- wanted to learn python

### Challenges:
- ATmega328P is an 8-bit MCU - does not support USB:HID out-of-the box - must realize a soft-USB-HID in arduino
- See if the board is also capable of driving an old hdd motor as an rotary encoder (feels go to roll it man)

### How does this work?

#### User control interface
The keypad (and the encoder later).
+ Based on UART first, the device shall transfer the pressed buttons labels: 1,2,3,4,5,6,7,8,9,0,*,#,A,B,C,D
+ Connection status should be indicated on an external LED

#### Host side
+ UART connection has to be established with a simple python terminal software (only printing what is received on COM-port)

### ToDo list:
- [x] UART-based simple keypad handler arduino project that prints the keys to the serial
- [ ] Host application that connects to the correct serial port and prints what is coming from it (py)
- [ ] Create basic communication protocol that is able to report the connection status (py)
- [ ] Update arduino project to indicate communication status on an external LED
- [ ] Automatic reconnect feature (py)

