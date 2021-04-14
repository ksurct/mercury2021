EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 3
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Sheet
S 3200 6650 1650 950 
U 6095675A
F0 "Sensors" 50
F1 "Sensors.sch" 50
F2 "SensorPower" I L 3200 6700 50 
$EndSheet
$Sheet
S 1100 6400 1500 1150
U 60979A3C
F0 "Motors" 50
F1 "Motors.sch" 50
F2 "MotorPower" I R 2600 6550 50 
$EndSheet
Wire Bus Line
	2600 6550 2950 6550
$Comp
L power:+5V #PWR0101
U 1 1 608755F4
P 1750 4300
F 0 "#PWR0101" H 1750 4150 50  0001 C CNN
F 1 "+5V" H 1765 4473 50  0001 C CNN
F 2 "" H 1750 4300 50  0001 C CNN
F 3 "" H 1750 4300 50  0001 C CNN
	1    1750 4300
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 60875F84
P 1450 4000
F 0 "#PWR0102" H 1450 3750 50  0001 C CNN
F 1 "GND" H 1455 3827 50  0001 C CNN
F 2 "" H 1450 4000 50  0001 C CNN
F 3 "" H 1450 4000 50  0001 C CNN
	1    1450 4000
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Linear:LM1084-5.0 U1
U 1 1 6087CEF6
P 1750 4000
F 0 "U1" V 1704 4105 50  0000 L CNN
F 1 "LM1084-5.0" V 1795 4105 50  0000 L CNN
F 2 "" H 1750 4250 50  0001 C CIN
F 3 "http://www.ti.com/lit/ds/symlink/lm1084.pdf" H 1750 4000 50  0001 C CNN
	1    1750 4000
	0    1    1    0   
$EndComp
Wire Wire Line
	1550 3700 1450 3700
Wire Wire Line
	1650 3700 1750 3700
Wire Wire Line
	1450 3700 1450 4000
Wire Wire Line
	1450 4000 2000 4000
Connection ~ 1450 4000
Wire Wire Line
	1750 3700 1900 3700
Connection ~ 1750 3700
Connection ~ 1750 4300
$Comp
L power:+BATT #PWR0103
U 1 1 6088B3F5
P 1750 3700
F 0 "#PWR0103" H 1750 3550 50  0001 C CNN
F 1 "+BATT" H 1850 3800 50  0001 C CNN
F 2 "" H 1750 3700 50  0001 C CNN
F 3 "" H 1750 3700 50  0001 C CNN
	1    1750 3700
	1    0    0    -1  
$EndComp
Text Label 2300 3700 0    50   ~ 0
11.1V
Text Label 2300 4000 0    50   ~ 0
GND
Text Label 2300 4300 0    50   ~ 0
5V
$Comp
L Device:CP C1
U 1 1 6088CA50
P 2000 3850
F 0 "C1" H 2118 3896 50  0000 L CNN
F 1 "10μf" H 2118 3805 50  0000 L CNN
F 2 "" H 2038 3700 50  0001 C CNN
F 3 "~" H 2000 3850 50  0001 C CNN
	1    2000 3850
	1    0    0    -1  
$EndComp
Connection ~ 2000 3700
Connection ~ 2000 4000
Wire Wire Line
	2000 4000 2600 4000
$Comp
L Connector:Screw_Terminal_01x02 J1
U 1 1 608781A8
P 1550 3500
F 0 "J1" V 1514 3312 50  0001 R CNN
F 1 "Batt_Power" V 1700 3850 50  0000 R CNN
F 2 "" H 1550 3500 50  0001 C CNN
F 3 "~" H 1550 3500 50  0001 C CNN
	1    1550 3500
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Conn_01x11_Male J7
U 1 1 6088EBF8
P 2750 4900
F 0 "J7" H 2722 4832 50  0000 R CNN
F 1 "Conn_01x11_Male" H 2722 4923 50  0000 R CNN
F 2 "" H 2750 4900 50  0001 C CNN
F 3 "~" H 2750 4900 50  0001 C CNN
	1    2750 4900
	-1   0    0    1   
$EndComp
Wire Wire Line
	2550 4300 2550 4400
Wire Wire Line
	2550 5400 2550 5500
Wire Wire Line
	2550 4400 2550 4500
Connection ~ 2550 4400
Wire Wire Line
	2550 4500 2550 4600
Connection ~ 2550 4500
Connection ~ 2550 5400
Connection ~ 2550 4600
Wire Wire Line
	2550 4600 2550 4700
Connection ~ 2550 4700
Wire Wire Line
	2550 4700 2550 4800
Connection ~ 2550 4800
Wire Wire Line
	2550 4800 2550 4900
Connection ~ 2550 4900
Wire Wire Line
	2550 4900 2550 5000
Connection ~ 2550 5000
Wire Wire Line
	2550 5000 2550 5100
Connection ~ 2550 5100
Wire Wire Line
	2550 5100 2550 5200
Connection ~ 2550 5200
Wire Wire Line
	2550 5200 2550 5300
Connection ~ 2550 5300
Wire Wire Line
	2550 5300 2550 5400
$Comp
L Connector:Conn_01x11_Male J8
U 1 1 6089FA96
P 3250 4600
F 0 "J8" H 3222 4532 50  0000 R CNN
F 1 "Conn_01x11_Male" H 3222 4623 50  0000 R CNN
F 2 "" H 3250 4600 50  0001 C CNN
F 3 "~" H 3250 4600 50  0001 C CNN
	1    3250 4600
	-1   0    0    1   
$EndComp
Wire Wire Line
	3050 4000 3050 4100
Wire Wire Line
	3050 4100 3050 4200
Connection ~ 3050 4100
Wire Wire Line
	3050 4200 3050 4300
Connection ~ 3050 4200
Connection ~ 3050 5100
Connection ~ 3050 4300
Wire Wire Line
	3050 4300 3050 4400
Connection ~ 3050 4400
Wire Wire Line
	3050 4400 3050 4500
Connection ~ 3050 4500
Wire Wire Line
	3050 4500 3050 4600
Connection ~ 3050 4600
Wire Wire Line
	3050 4600 3050 4700
Connection ~ 3050 4700
Wire Wire Line
	3050 4700 3050 4800
Connection ~ 3050 4800
Wire Wire Line
	3050 4800 3050 4900
Connection ~ 3050 4900
Wire Wire Line
	3050 4900 3050 5000
Connection ~ 3050 5000
Wire Wire Line
	3050 5000 3050 5100
$Comp
L Connector:Conn_01x11_Male J14
U 1 1 608A2E6C
P 3750 4300
F 0 "J14" H 3722 4232 50  0000 R CNN
F 1 "Conn_01x11_Male" H 3722 4323 50  0000 R CNN
F 2 "" H 3750 4300 50  0001 C CNN
F 3 "~" H 3750 4300 50  0001 C CNN
	1    3750 4300
	-1   0    0    1   
$EndComp
Wire Wire Line
	3550 3700 3550 3800
Wire Wire Line
	3550 3800 3550 3900
Connection ~ 3550 3800
Wire Wire Line
	3550 3900 3550 4000
Connection ~ 3550 3900
Connection ~ 3550 4800
Connection ~ 3550 4000
Wire Wire Line
	3550 4000 3550 4100
Connection ~ 3550 4100
Wire Wire Line
	3550 4100 3550 4200
Connection ~ 3550 4200
Wire Wire Line
	3550 4200 3550 4300
Connection ~ 3550 4300
Wire Wire Line
	3550 4300 3550 4400
Connection ~ 3550 4400
Wire Wire Line
	3550 4400 3550 4500
Connection ~ 3550 4500
Wire Wire Line
	3550 4500 3550 4600
Connection ~ 3550 4600
Wire Wire Line
	3550 4600 3550 4700
Connection ~ 3550 4700
Wire Wire Line
	3550 4700 3550 4800
Wire Wire Line
	3550 4800 3550 4900
Wire Wire Line
	2550 5500 2750 5500
Connection ~ 2550 5500
Wire Wire Line
	2550 5500 2550 5600
Text Label 2600 5500 0    50   ~ 0
VDD0
Wire Wire Line
	3050 5100 3050 5200
Wire Wire Line
	3050 5200 3250 5200
Connection ~ 3050 5200
Wire Wire Line
	3050 5200 3050 5300
Text Label 3100 5200 0    50   ~ 0
GND0
Wire Wire Line
	3050 5300 3250 5300
Text Label 3100 5300 0    50   ~ 0
GND1
Wire Wire Line
	3050 5400 3250 5400
Text Label 3100 5400 0    50   ~ 0
GND2
Wire Wire Line
	3050 5500 3250 5500
Text Label 3100 5500 0    50   ~ 0
GND3
Wire Wire Line
	3050 5600 3250 5600
Text Label 3100 5600 0    50   ~ 0
GND4
Wire Wire Line
	3050 5700 3250 5700
Text Label 3100 5700 0    50   ~ 0
GND5
Wire Wire Line
	3050 5800 3250 5800
Text Label 3100 5800 0    50   ~ 0
GND6
Wire Wire Line
	3050 5900 3250 5900
Text Label 3100 5900 0    50   ~ 0
GND7
Wire Wire Line
	3050 5300 3050 5400
Connection ~ 3050 5300
Connection ~ 3050 5400
Wire Wire Line
	3050 5400 3050 5500
Connection ~ 3050 5500
Wire Wire Line
	3050 5500 3050 5600
Connection ~ 3050 5600
Wire Wire Line
	3050 5600 3050 5700
Connection ~ 3050 5700
Wire Wire Line
	3050 5700 3050 5800
Connection ~ 3050 5800
Wire Wire Line
	3050 5800 3050 5900
Wire Wire Line
	2550 5600 2750 5600
Text Label 2600 5600 0    50   ~ 0
VDD1
Wire Wire Line
	2550 5700 2750 5700
Text Label 2600 5700 0    50   ~ 0
VDD2
Wire Wire Line
	2550 5800 2750 5800
Text Label 2600 5800 0    50   ~ 0
VDD3
Wire Wire Line
	2550 5900 2750 5900
Text Label 2600 5900 0    50   ~ 0
VDD4
Wire Wire Line
	2550 6000 2750 6000
Text Label 2600 6000 0    50   ~ 0
VDD5
Wire Wire Line
	2550 6100 2750 6100
Text Label 2600 6100 0    50   ~ 0
VDD6
Wire Wire Line
	2550 6200 2750 6200
Text Label 2600 6200 0    50   ~ 0
VDD7
Wire Wire Line
	2550 5600 2550 5700
Connection ~ 2550 5600
Connection ~ 2550 5700
Wire Wire Line
	2550 5700 2550 5800
Connection ~ 2550 5800
Wire Wire Line
	2550 5800 2550 5900
Connection ~ 2550 5900
Wire Wire Line
	2550 5900 2550 6000
Connection ~ 2550 6000
Wire Wire Line
	2550 6000 2550 6100
Connection ~ 2550 6100
Wire Wire Line
	2550 6100 2550 6200
Entry Wire Line
	2750 5500 2850 5600
Entry Wire Line
	2750 5600 2850 5700
Entry Wire Line
	2750 5700 2850 5800
Entry Wire Line
	2750 5800 2850 5900
Entry Wire Line
	2750 5900 2850 6000
Entry Wire Line
	2750 6000 2850 6100
Entry Wire Line
	2750 6100 2850 6200
Entry Wire Line
	2750 6200 2850 6300
Entry Wire Line
	3250 5200 3350 5300
Entry Wire Line
	3250 5300 3350 5400
Entry Wire Line
	3250 5400 3350 5500
Entry Wire Line
	3250 5500 3350 5600
Entry Wire Line
	3250 5600 3350 5700
Entry Wire Line
	3250 5700 3350 5800
Entry Wire Line
	3250 5800 3350 5900
Entry Wire Line
	3250 5900 3350 6000
Wire Bus Line
	2850 6050 2950 6050
Connection ~ 2850 6050
Connection ~ 2950 6050
Wire Wire Line
	2550 6200 2550 6300
Wire Wire Line
	2550 6300 2750 6300
Connection ~ 2550 6200
Entry Wire Line
	2750 6300 2850 6400
Text Label 2600 6300 0    50   ~ 0
MP_+5V
Wire Wire Line
	3050 5900 3050 6000
Text Label 3100 6000 0    50   ~ 0
MP_GND
Connection ~ 3050 5900
Entry Wire Line
	3700 5000 3800 5100
Entry Wire Line
	3700 5100 3800 5200
Wire Wire Line
	3550 5000 3700 5000
Wire Wire Line
	3550 5100 3700 5100
Wire Wire Line
	3550 4900 3700 4900
Text Label 3600 5000 0    50   ~ 0
RM_VIN
Text Label 3600 5100 0    50   ~ 0
Servo_VIN
Text Label 3600 4900 0    50   ~ 0
LM_VIN
Entry Wire Line
	3700 4900 3800 5000
Connection ~ 3350 6050
Wire Wire Line
	3050 6000 3250 6000
Wire Bus Line
	2950 6050 3350 6050
Text Label 3100 6200 0    50   ~ 0
LM_GND
Text Label 3100 6100 0    50   ~ 0
Servo_GND
Entry Wire Line
	3250 6300 3350 6400
Entry Wire Line
	3250 6000 3350 6100
Wire Wire Line
	3050 6100 3250 6100
Wire Wire Line
	3050 6200 3250 6200
Wire Wire Line
	3050 6300 3250 6300
Wire Wire Line
	3050 6000 3050 6100
Connection ~ 3050 6000
Connection ~ 3050 6100
Wire Wire Line
	3050 6100 3050 6200
Text Label 3150 6300 0    50   ~ 0
RM_GND
Wire Wire Line
	3050 6200 3050 6300
Connection ~ 3050 6200
Entry Wire Line
	3250 6100 3350 6200
Entry Wire Line
	3250 6200 3350 6300
Connection ~ 3550 4900
Wire Wire Line
	3550 4900 3550 5000
Wire Wire Line
	3550 5000 3550 5100
Connection ~ 3550 5000
Wire Bus Line
	3800 6050 3350 6050
Wire Bus Line
	2950 6550 2950 6050
Wire Bus Line
	3200 6700 2950 6700
Wire Bus Line
	2950 6700 2950 6550
Connection ~ 2950 6550
$Comp
L Connector:Screw_Terminal_01x02 J13
U 1 1 6093E999
P 4600 3550
F 0 "J13" H 4680 3542 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 4680 3451 50  0000 L CNN
F 2 "" H 4600 3550 50  0001 C CNN
F 3 "~" H 4600 3550 50  0001 C CNN
	1    4600 3550
	0    1    1    0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J12
U 1 1 609409E0
P 4850 3550
F 0 "J12" H 4930 3542 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 4930 3451 50  0000 L CNN
F 2 "" H 4850 3550 50  0001 C CNN
F 3 "~" H 4850 3550 50  0001 C CNN
	1    4850 3550
	0    1    1    0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J11
U 1 1 60940C70
P 5100 3550
F 0 "J11" H 5180 3542 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 5180 3451 50  0000 L CNN
F 2 "" H 5100 3550 50  0001 C CNN
F 3 "~" H 5100 3550 50  0001 C CNN
	1    5100 3550
	0    1    1    0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J10
U 1 1 60941108
P 5350 3550
F 0 "J10" H 5430 3542 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 5430 3451 50  0000 L CNN
F 2 "" H 5350 3550 50  0001 C CNN
F 3 "~" H 5350 3550 50  0001 C CNN
	1    5350 3550
	0    1    1    0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J9
U 1 1 609414F6
P 5600 3550
F 0 "J9" H 5680 3542 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 5680 3451 50  0000 L CNN
F 2 "" H 5600 3550 50  0001 C CNN
F 3 "~" H 5600 3550 50  0001 C CNN
	1    5600 3550
	0    1    1    0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J2
U 1 1 60941AB4
P 5500 2250
F 0 "J2" H 5418 1925 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 5418 2016 50  0000 C CNN
F 2 "" H 5500 2250 50  0001 C CNN
F 3 "~" H 5500 2250 50  0001 C CNN
	1    5500 2250
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J3
U 1 1 60942614
P 5250 2250
F 0 "J3" H 5168 1925 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 5168 2016 50  0000 C CNN
F 2 "" H 5250 2250 50  0001 C CNN
F 3 "~" H 5250 2250 50  0001 C CNN
	1    5250 2250
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J4
U 1 1 60942A20
P 5000 2250
F 0 "J4" H 4918 1925 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 4918 2016 50  0000 C CNN
F 2 "" H 5000 2250 50  0001 C CNN
F 3 "~" H 5000 2250 50  0001 C CNN
	1    5000 2250
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J5
U 1 1 6094314E
P 4750 2250
F 0 "J5" H 4668 1925 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 4668 2016 50  0000 C CNN
F 2 "" H 4750 2250 50  0001 C CNN
F 3 "~" H 4750 2250 50  0001 C CNN
	1    4750 2250
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J6
U 1 1 609434ED
P 4500 2250
F 0 "J6" H 4418 1925 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 4418 2016 50  0000 C CNN
F 2 "" H 4500 2250 50  0001 C CNN
F 3 "~" H 4500 2250 50  0001 C CNN
	1    4500 2250
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2550 4300 2700 4300
Wire Wire Line
	5600 2600 5600 2450
Connection ~ 2550 4300
Wire Wire Line
	5350 2450 5350 2600
Connection ~ 5350 2600
Wire Wire Line
	5350 2600 5600 2600
Wire Wire Line
	5100 2450 5100 2600
Connection ~ 5100 2600
Wire Wire Line
	5100 2600 5350 2600
Wire Wire Line
	4850 2450 4850 2600
Connection ~ 4850 2600
Wire Wire Line
	4850 2600 5100 2600
Wire Wire Line
	4600 2450 4600 2600
Connection ~ 4600 2600
Wire Wire Line
	4600 2600 4850 2600
Wire Wire Line
	5500 2950 5500 2450
Wire Wire Line
	5250 2450 5250 2950
Connection ~ 5250 2950
Wire Wire Line
	5250 2950 5500 2950
Wire Wire Line
	5000 2450 5000 2950
Connection ~ 5000 2950
Wire Wire Line
	5000 2950 5250 2950
Wire Wire Line
	4750 2450 4750 2950
Connection ~ 4750 2950
Wire Wire Line
	4750 2950 5000 2950
Wire Wire Line
	4500 2450 4500 2950
Connection ~ 4500 2950
Wire Wire Line
	4500 2950 4750 2950
Wire Wire Line
	5600 3250 5600 3350
Wire Wire Line
	5350 3250 5350 3350
Connection ~ 5350 3250
Wire Wire Line
	5350 3250 5600 3250
Wire Wire Line
	5100 3350 5100 3250
Connection ~ 5100 3250
Wire Wire Line
	5100 3250 5350 3250
Wire Wire Line
	4850 3350 4850 3250
Connection ~ 4850 3250
Wire Wire Line
	4850 3250 5100 3250
Wire Wire Line
	4600 3350 4600 3250
Connection ~ 4600 3250
Wire Wire Line
	4600 3250 4850 3250
Wire Wire Line
	5500 2950 5500 3350
Connection ~ 5500 2950
Wire Wire Line
	5250 2950 5250 3350
Wire Wire Line
	5000 2950 5000 3350
Wire Wire Line
	4750 2950 4750 3350
Wire Wire Line
	4500 2950 4500 3350
$Comp
L Regulator_Linear:LM1084-3.3 U?
U 1 1 60D85B5C
P 1900 3400
F 0 "U?" V 1946 3505 50  0000 L CNN
F 1 "LM1084-3.3" V 1855 3505 50  0000 L CNN
F 2 "" H 1900 3650 50  0001 C CIN
F 3 "http://www.ti.com/lit/ds/symlink/lm1084.pdf" H 1900 3400 50  0001 C CNN
	1    1900 3400
	0    -1   -1   0   
$EndComp
$Comp
L Device:CP C?
U 1 1 60D8BE94
P 2000 4150
F 0 "C?" H 1882 4104 50  0000 R CNN
F 1 "10μf" H 1882 4195 50  0000 R CNN
F 2 "" H 2038 4000 50  0001 C CNN
F 3 "~" H 2000 4150 50  0001 C CNN
	1    2000 4150
	-1   0    0    1   
$EndComp
Connection ~ 1900 3700
Wire Wire Line
	1900 3700 2000 3700
Wire Wire Line
	2000 3700 2250 3700
$Comp
L Device:CP C?
U 1 1 60DFA77E
P 2250 3550
F 0 "C?" H 2132 3504 50  0000 R CNN
F 1 "10μf" H 2132 3595 50  0000 R CNN
F 2 "" H 2288 3400 50  0001 C CNN
F 3 "~" H 2250 3550 50  0001 C CNN
	1    2250 3550
	-1   0    0    1   
$EndComp
$Comp
L Device:CP C?
U 1 1 60DFEA28
P 2250 3250
F 0 "C?" H 2368 3296 50  0000 L CNN
F 1 "10μf" H 2368 3205 50  0000 L CNN
F 2 "" H 2288 3100 50  0001 C CNN
F 3 "~" H 2250 3250 50  0001 C CNN
	1    2250 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	1750 4300 2000 4300
Connection ~ 2000 4300
Wire Wire Line
	2000 4300 2550 4300
Connection ~ 2250 3700
Wire Wire Line
	2250 3700 3550 3700
Wire Wire Line
	1900 3100 2250 3100
$Comp
L power:+3.3V #PWR?
U 1 1 60E16566
P 1900 3100
F 0 "#PWR?" H 1900 2950 50  0001 C CNN
F 1 "+3.3V" H 1915 3273 50  0000 C CNN
F 2 "" H 1900 3100 50  0001 C CNN
F 3 "" H 1900 3100 50  0001 C CNN
	1    1900 3100
	1    0    0    -1  
$EndComp
Connection ~ 1900 3100
Connection ~ 2250 3100
$Comp
L Connector:Conn_01x11_Male J?
U 1 1 60E1FDA6
P 4100 4000
F 0 "J?" H 4072 3932 50  0000 R CNN
F 1 "Conn_01x11_Male" H 4072 4023 50  0000 R CNN
F 2 "" H 4100 4000 50  0001 C CNN
F 3 "~" H 4100 4000 50  0001 C CNN
	1    4100 4000
	-1   0    0    1   
$EndComp
Wire Wire Line
	3900 3500 3900 3600
Connection ~ 3900 3500
Wire Wire Line
	3900 3600 3900 3700
Connection ~ 3900 3600
Connection ~ 3900 4500
Connection ~ 3900 3700
Wire Wire Line
	3900 3700 3900 3800
Connection ~ 3900 3800
Wire Wire Line
	3900 3800 3900 3900
Connection ~ 3900 3900
Wire Wire Line
	3900 3900 3900 4000
Connection ~ 3900 4000
Wire Wire Line
	3900 4000 3900 4100
Connection ~ 3900 4100
Wire Wire Line
	3900 4100 3900 4200
Connection ~ 3900 4200
Wire Wire Line
	3900 4200 3900 4300
Connection ~ 3900 4300
Wire Wire Line
	3900 4300 3900 4400
Connection ~ 3900 4400
Wire Wire Line
	3900 4400 3900 4500
Wire Wire Line
	3900 4500 3900 4600
Text Label 3950 4600 0    50   ~ 0
LM_VIN
Wire Wire Line
	3900 3100 3900 3500
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60E3AE94
P 2250 1900
F 0 "J?" H 2168 1575 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2168 1666 50  0000 C CNN
F 2 "" H 2250 1900 50  0001 C CNN
F 3 "~" H 2250 1900 50  0001 C CNN
	1    2250 1900
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60E3AE9A
P 2250 2150
F 0 "J?" H 2168 1825 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2168 1916 50  0000 C CNN
F 2 "" H 2250 2150 50  0001 C CNN
F 3 "~" H 2250 2150 50  0001 C CNN
	1    2250 2150
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60E3AEA0
P 2250 2400
F 0 "J?" H 2168 2075 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2168 2166 50  0000 C CNN
F 2 "" H 2250 2400 50  0001 C CNN
F 3 "~" H 2250 2400 50  0001 C CNN
	1    2250 2400
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60E3AEA6
P 2250 2650
F 0 "J?" H 2168 2325 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2168 2416 50  0000 C CNN
F 2 "" H 2250 2650 50  0001 C CNN
F 3 "~" H 2250 2650 50  0001 C CNN
	1    2250 2650
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60E3AEAC
P 2250 2900
F 0 "J?" H 2168 2575 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2168 2666 50  0000 C CNN
F 2 "" H 2250 2900 50  0001 C CNN
F 3 "~" H 2250 2900 50  0001 C CNN
	1    2250 2900
	-1   0    0    1   
$EndComp
Wire Wire Line
	2600 1800 2450 1800
Wire Wire Line
	2450 2050 2600 2050
Connection ~ 2600 2050
Wire Wire Line
	2600 2050 2600 1800
Wire Wire Line
	2450 2300 2600 2300
Connection ~ 2600 2300
Wire Wire Line
	2600 2300 2600 2050
Wire Wire Line
	2450 2550 2600 2550
Connection ~ 2600 2550
Wire Wire Line
	2600 2550 2600 2300
Wire Wire Line
	2450 2800 2600 2800
Connection ~ 2600 2800
Wire Wire Line
	2600 2800 2600 2550
Wire Wire Line
	2950 1900 2450 1900
Wire Wire Line
	2450 2150 2950 2150
Connection ~ 2950 2150
Wire Wire Line
	2950 2150 2950 1900
Wire Wire Line
	2450 2400 2950 2400
Connection ~ 2950 2400
Wire Wire Line
	2950 2400 2950 2150
Wire Wire Line
	2450 2650 2950 2650
Connection ~ 2950 2650
Wire Wire Line
	2950 2650 2950 2400
Wire Wire Line
	2450 2900 2950 2900
Connection ~ 2950 2900
Wire Wire Line
	2950 2900 2950 2650
Wire Wire Line
	2950 2900 2950 3100
Connection ~ 2950 3100
Wire Wire Line
	2950 3100 3150 3100
Connection ~ 2600 4000
Wire Wire Line
	2250 3100 2950 3100
Wire Wire Line
	2600 2800 2600 4000
Wire Wire Line
	2600 4000 3050 4000
Wire Wire Line
	3050 2950 3050 4000
Wire Wire Line
	3050 2950 4500 2950
Connection ~ 3050 4000
Wire Wire Line
	3150 2600 3150 3100
Wire Wire Line
	3150 2600 4600 2600
Connection ~ 3150 3100
Wire Wire Line
	3150 3100 3900 3100
Wire Wire Line
	2550 3250 2550 4300
Wire Wire Line
	2550 3250 4600 3250
Wire Bus Line
	3800 5000 3800 6050
Wire Bus Line
	3350 6050 3350 6400
Wire Bus Line
	2850 6050 2850 6400
Wire Bus Line
	2850 5600 2850 6050
Wire Bus Line
	3350 5300 3350 6050
$EndSCHEMATC
