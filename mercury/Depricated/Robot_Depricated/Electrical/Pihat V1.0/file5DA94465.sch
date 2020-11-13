EESchema Schematic File Version 4
LIBS:Pihat V1.0-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 5
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
L Connector:Raspberry_Pi_2_3 J?
U 1 1 5DA9760A
P 5800 4000
F 0 "J?" H 5800 4600 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 5800 4700 50  0000 C CNN
F 2 "" H 5800 4000 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 5800 4000 50  0001 C CNN
	1    5800 4000
	1    0    0    -1  
$EndComp
Text GLabel 4750 3100 0    50   Input ~ 0
PiTx
Wire Wire Line
	5000 3100 4750 3100
Text GLabel 4750 3200 0    50   Input ~ 0
PiRx
Wire Wire Line
	5000 3200 4750 3200
$Comp
L power:GND #PWR?
U 1 1 5DA9BCF9
P 5700 5700
F 0 "#PWR?" H 5700 5450 50  0001 C CNN
F 1 "GND" H 5705 5527 50  0000 C CNN
F 2 "" H 5700 5700 50  0001 C CNN
F 3 "" H 5700 5700 50  0001 C CNN
	1    5700 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 5300 5400 5550
Wire Wire Line
	5400 5550 5500 5550
Wire Wire Line
	5700 5550 5700 5700
Wire Wire Line
	6100 5300 6100 5550
Wire Wire Line
	6100 5550 6000 5550
Connection ~ 5700 5550
Wire Wire Line
	5500 5300 5500 5550
Connection ~ 5500 5550
Wire Wire Line
	5500 5550 5600 5550
Wire Wire Line
	5600 5300 5600 5550
Connection ~ 5600 5550
Wire Wire Line
	5600 5550 5700 5550
Wire Wire Line
	5700 5300 5700 5550
Wire Wire Line
	5800 5300 5800 5550
Connection ~ 5800 5550
Wire Wire Line
	5800 5550 5700 5550
Wire Wire Line
	5900 5300 5900 5550
Connection ~ 5900 5550
Wire Wire Line
	5900 5550 5800 5550
Wire Wire Line
	6000 5300 6000 5550
Connection ~ 6000 5550
Wire Wire Line
	6000 5550 5900 5550
$Comp
L power:+5V #PWR?
U 1 1 5DA9D797
P 5600 2500
F 0 "#PWR?" H 5600 2350 50  0001 C CNN
F 1 "+5V" H 5615 2673 50  0000 C CNN
F 2 "" H 5600 2500 50  0001 C CNN
F 3 "" H 5600 2500 50  0001 C CNN
	1    5600 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 2500 5600 2600
Wire Wire Line
	5600 2600 5700 2600
Wire Wire Line
	5700 2600 5700 2700
Connection ~ 5600 2600
Wire Wire Line
	5600 2600 5600 2700
$EndSCHEMATC
