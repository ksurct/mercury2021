import i2clcd
import subprocess

#initilize the lcd screen for i2c
lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=16)
lcd.init()
ip = str(subprocess.check_output(['hostname', '-I'])).split(' ')[0].replace("b'", "")

#Find the IP
from time import sleep
#If IP address is a flop
while (ip == r"\n'"):
    ip = str(subprocess.check_output(['hostname', '-I'])).split(' ')[0].replace("b'", "")
    print("IP:",ip)
    lcd.print_line("Couldn't find IP", line=0, align='CENTER')
    lcd.print_line("Offline?", line=1, align= 'CENTER')
    sleep(1)
lcd.print_line("My Boi's IP:", line=0, align='CENTER')
lcd.print_line(ip, line=1, align='CENTER')
