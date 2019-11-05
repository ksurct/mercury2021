EESchema Schematic File Version 4
LIBS:Pihat V1.0-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 5
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
L Connector:Conn_01x04_Male J?
U 1 1 5DB2AF84
P 1950 1600
F 0 "J?" H 2058 1881 50  0000 C CNN
F 1 "Conn_01x04_Male" V 1900 1600 50  0000 C CNN
F 2 "" H 1950 1600 50  0001 C CNN
F 3 "~" H 1950 1600 50  0001 C CNN
	1    1950 1600
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5DB2AF8A
P 2300 1950
F 0 "#PWR?" H 2300 1700 50  0001 C CNN
F 1 "GND" H 2305 1777 50  0000 C CNN
F 2 "" H 2300 1950 50  0001 C CNN
F 3 "" H 2300 1950 50  0001 C CNN
	1    2300 1950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5DB2AF90
P 2300 1350
F 0 "#PWR?" H 2300 1100 50  0001 C CNN
F 1 "GND" H 2305 1177 50  0000 C CNN
F 2 "" H 2300 1350 50  0001 C CNN
F 3 "" H 2300 1350 50  0001 C CNN
	1    2300 1350
	-1   0    0    1   
$EndComp
Wire Wire Line
	2150 1500 2300 1500
Wire Wire Line
	2300 1500 2300 1350
Wire Wire Line
	2150 1800 2300 1800
Wire Wire Line
	2300 1800 2300 1950
$Comp
L power:+5V #PWR?
U 1 1 5DB2AF9A
P 2350 1700
F 0 "#PWR?" H 2350 1550 50  0001 C CNN
F 1 "+5V" V 2365 1828 50  0000 L CNN
F 2 "" H 2350 1700 50  0001 C CNN
F 3 "" H 2350 1700 50  0001 C CNN
	1    2350 1700
	0    1    1    0   
$EndComp
Wire Wire Line
	2150 1700 2350 1700
Text GLabel 2350 1600 2    50   Input ~ 0
LEDData
Wire Wire Line
	2150 1600 2350 1600
$EndSCHEMATC
