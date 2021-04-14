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
	1750 3700 2000 3700
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
L Device:C C1
U 1 1 6088CA50
P 2000 3850
F 0 "C1" H 2115 3896 50  0000 L CNN
F 1 "10μf" H 2115 3805 50  0000 L CNN
F 2 "" H 2038 3700 50  0001 C CNN
F 3 "~" H 2000 3850 50  0001 C CNN
	1    2000 3850
	1    0    0    -1  
$EndComp
Connection ~ 2000 3700
Connection ~ 2000 4000
$Comp
L Device:C C2
U 1 1 6088D347
P 2000 4150
F 0 "C2" H 2115 4196 50  0000 L CNN
F 1 "10μf" H 2115 4105 50  0000 L CNN
F 2 "" H 2038 4000 50  0001 C CNN
F 3 "~" H 2000 4150 50  0001 C CNN
	1    2000 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	1750 4300 2000 4300
Connection ~ 2000 4300
Wire Wire Line
	2000 4300 2550 4300
Wire Wire Line
	2000 4000 3050 4000
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
P 3650 3250
F 0 "J13" H 3730 3242 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 3730 3151 50  0000 L CNN
F 2 "" H 3650 3250 50  0001 C CNN
F 3 "~" H 3650 3250 50  0001 C CNN
	1    3650 3250
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J12
U 1 1 609409E0
P 3650 3000
F 0 "J12" H 3730 2992 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 3730 2901 50  0000 L CNN
F 2 "" H 3650 3000 50  0001 C CNN
F 3 "~" H 3650 3000 50  0001 C CNN
	1    3650 3000
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J11
U 1 1 60940C70
P 3650 2750
F 0 "J11" H 3730 2742 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 3730 2651 50  0000 L CNN
F 2 "" H 3650 2750 50  0001 C CNN
F 3 "~" H 3650 2750 50  0001 C CNN
	1    3650 2750
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J10
U 1 1 60941108
P 3650 2500
F 0 "J10" H 3730 2492 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 3730 2401 50  0000 L CNN
F 2 "" H 3650 2500 50  0001 C CNN
F 3 "~" H 3650 2500 50  0001 C CNN
	1    3650 2500
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J9
U 1 1 609414F6
P 3650 2250
F 0 "J9" H 3730 2242 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 3730 2151 50  0000 L CNN
F 2 "" H 3650 2250 50  0001 C CNN
F 3 "~" H 3650 2250 50  0001 C CNN
	1    3650 2250
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J2
U 1 1 60941AB4
P 2350 2350
F 0 "J2" H 2268 2025 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2268 2116 50  0000 C CNN
F 2 "" H 2350 2350 50  0001 C CNN
F 3 "~" H 2350 2350 50  0001 C CNN
	1    2350 2350
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J3
U 1 1 60942614
P 2350 2600
F 0 "J3" H 2268 2275 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2268 2366 50  0000 C CNN
F 2 "" H 2350 2600 50  0001 C CNN
F 3 "~" H 2350 2600 50  0001 C CNN
	1    2350 2600
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J4
U 1 1 60942A20
P 2350 2850
F 0 "J4" H 2268 2525 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2268 2616 50  0000 C CNN
F 2 "" H 2350 2850 50  0001 C CNN
F 3 "~" H 2350 2850 50  0001 C CNN
	1    2350 2850
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J5
U 1 1 6094314E
P 2350 3100
F 0 "J5" H 2268 2775 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2268 2866 50  0000 C CNN
F 2 "" H 2350 3100 50  0001 C CNN
F 3 "~" H 2350 3100 50  0001 C CNN
	1    2350 3100
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J6
U 1 1 609434ED
P 2350 3350
F 0 "J6" H 2268 3025 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2268 3116 50  0000 C CNN
F 2 "" H 2350 3350 50  0001 C CNN
F 3 "~" H 2350 3350 50  0001 C CNN
	1    2350 3350
	-1   0    0    1   
$EndComp
Wire Wire Line
	2550 4300 2700 4300
Wire Wire Line
	2700 4300 2700 3250
Wire Wire Line
	2700 2250 2550 2250
Connection ~ 2550 4300
Wire Wire Line
	2550 2500 2700 2500
Connection ~ 2700 2500
Wire Wire Line
	2700 2500 2700 2250
Wire Wire Line
	2550 2750 2700 2750
Connection ~ 2700 2750
Wire Wire Line
	2700 2750 2700 2500
Wire Wire Line
	2550 3000 2700 3000
Connection ~ 2700 3000
Wire Wire Line
	2700 3000 2700 2750
Wire Wire Line
	2550 3250 2700 3250
Connection ~ 2700 3250
Wire Wire Line
	2700 3250 2700 3000
Wire Wire Line
	3050 4000 3050 3350
Wire Wire Line
	3050 2350 2550 2350
Connection ~ 3050 4000
Wire Wire Line
	2550 2600 3050 2600
Connection ~ 3050 2600
Wire Wire Line
	3050 2600 3050 2350
Wire Wire Line
	2550 2850 3050 2850
Connection ~ 3050 2850
Wire Wire Line
	3050 2850 3050 2600
Wire Wire Line
	2550 3100 3050 3100
Connection ~ 3050 3100
Wire Wire Line
	3050 3100 3050 2850
Wire Wire Line
	2550 3350 3050 3350
Connection ~ 3050 3350
Wire Wire Line
	3050 3350 3050 3100
Wire Wire Line
	3350 3700 3350 3250
Wire Wire Line
	3350 2250 3450 2250
Wire Wire Line
	3350 2500 3450 2500
Connection ~ 3350 2500
Wire Wire Line
	3350 2500 3350 2250
Wire Wire Line
	3450 2750 3350 2750
Connection ~ 3350 2750
Wire Wire Line
	3350 2750 3350 2500
Wire Wire Line
	3450 3000 3350 3000
Connection ~ 3350 3000
Wire Wire Line
	3350 3000 3350 2750
Wire Wire Line
	3450 3250 3350 3250
Connection ~ 3350 3250
Wire Wire Line
	3350 3250 3350 3000
Connection ~ 3350 3700
Wire Wire Line
	3350 3700 3550 3700
Wire Wire Line
	2000 3700 3350 3700
Wire Wire Line
	3050 2350 3450 2350
Connection ~ 3050 2350
Wire Wire Line
	3050 2600 3450 2600
Wire Wire Line
	3050 2850 3450 2850
Wire Wire Line
	3050 3100 3450 3100
Wire Wire Line
	3050 3350 3450 3350
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
