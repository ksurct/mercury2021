EESchema Schematic File Version 4
LIBS:Pihat V1.0-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 5
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L power:GND #PWR?
U 1 1 5DA99F5B
P 5650 5200
F 0 "#PWR?" H 5650 4950 50  0001 C CNN
F 1 "GND" H 5655 5027 50  0000 C CNN
F 2 "" H 5650 5200 50  0001 C CNN
F 3 "" H 5650 5200 50  0001 C CNN
	1    5650 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 5000 5600 5100
Wire Wire Line
	5600 5100 5650 5100
Wire Wire Line
	5650 5100 5650 5200
Wire Wire Line
	5700 5000 5700 5100
Wire Wire Line
	5700 5100 5650 5100
Connection ~ 5650 5100
$Comp
L power:+12V #PWR?
U 1 1 5DA9A991
P 5500 2750
F 0 "#PWR?" H 5500 2600 50  0001 C CNN
F 1 "+12V" H 5515 2923 50  0000 C CNN
F 2 "" H 5500 2750 50  0001 C CNN
F 3 "" H 5500 2750 50  0001 C CNN
	1    5500 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5500 2750 5500 3000
$Comp
L MCU_Module:Arduino_Nano_v3.x A?
U 1 1 5DA9909E
P 5600 4000
F 0 "A?" H 5600 4500 50  0000 C CNN
F 1 "Arduino_Nano_v3.x" V 5600 4000 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 5750 3050 50  0001 L CNN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 5600 3000 50  0001 C CNN
	1    5600 4000
	1    0    0    -1  
$EndComp
NoConn ~ 5700 3000
NoConn ~ 5800 3000
NoConn ~ 6100 3400
NoConn ~ 6100 3500
NoConn ~ 6100 3800
Text GLabel 4900 3400 0    50   Input ~ 0
PiTx
Text GLabel 4900 3500 0    50   Input ~ 0
PiRx
Wire Wire Line
	4900 3400 5100 3400
Wire Wire Line
	4900 3500 5100 3500
$EndSCHEMATC
