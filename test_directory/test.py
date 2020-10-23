import serial

serialport = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)

while True:
    serialport.write("rnSay something:")
    rcv = serialport.read(10)
    serialport.write("rnYou sent:" + repr(rcv))
    print(rcv)
