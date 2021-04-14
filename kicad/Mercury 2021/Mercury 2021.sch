EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 4
Title "Mercury 2021 Motherboard"
Date "2021-04-14"
Rev "2.0 Alpha"
Comp "Kansas State University Robotics Competition Team"
Comment1 "// plan to add credits for team in these comment lines at some point soon. "
Comment2 "// "
Comment3 "// "
Comment4 "https://github.com/ksurct/mercury2021/issues/10"
$EndDescr
$Sheet
S 4500 4050 1500 1150
U 60979A3C
F0 "Motors" 50
F1 "Motors.sch" 50
F2 "MotorPower" I R 6000 4200 50 
F3 "USB_BUS" I L 4500 4150 50 
$EndSheet
$Sheet
S 6850 2450 2100 1750
U 60E98AAB
F0 "Power" 50
F1 "Power.sch" 50
F2 "PowerBus" I L 6850 4000 50 
$EndSheet
Entry Bus Bus
	6000 3400 6100 3500
Entry Bus Bus
	6000 4200 6100 4300
Wire Bus Line
	6150 4000 6800 4000
Wire Bus Line
	6150 4000 6150 4300
Wire Bus Line
	6150 4300 6100 4300
Connection ~ 6150 4000
Wire Bus Line
	6100 3500 6150 3500
Wire Bus Line
	6150 3500 6150 4000
$Sheet
S 4350 2500 1650 1000
U 6095675A
F0 "Sensors" 50
F1 "Sensors.sch" 50
F2 "SensorPower" I R 6000 3400 50 
F3 "USB_BUS" I L 4350 3200 50 
$EndSheet
Wire Bus Line
	4500 4150 4100 4150
Wire Bus Line
	4100 4150 4100 3300
Wire Bus Line
	4100 3300 4300 3300
Wire Bus Line
	4350 3200 4300 3200
Wire Bus Line
	4300 3200 4300 3300
$EndSCHEMATC
