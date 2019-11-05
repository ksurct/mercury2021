EESchema Schematic File Version 4
LIBS:Pihat V1.0-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 5 5
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
L Mercury_Parts:Buck_Converters U?
U 1 1 5DB2B704
P 8500 5050
F 0 "U?" H 8475 5715 50  0000 C CNN
F 1 "Buck_Converters" H 8475 5624 50  0000 C CNN
F 2 "" H 8500 5650 50  0001 C CNN
F 3 "" H 8500 5650 50  0001 C CNN
	1    8500 5050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5DB2C263
P 9050 5300
F 0 "#PWR?" H 9050 5050 50  0001 C CNN
F 1 "GND" H 9055 5127 50  0000 C CNN
F 2 "" H 9050 5300 50  0001 C CNN
F 3 "" H 9050 5300 50  0001 C CNN
	1    9050 5300
	1    0    0    -1  
$EndComp
Wire Wire Line
	8850 4700 9050 4700
Wire Wire Line
	9050 4700 9050 5150
Wire Wire Line
	8850 5150 9050 5150
Connection ~ 9050 5150
Wire Wire Line
	9050 5150 9050 5300
$Comp
L power:+5V #PWR?
U 1 1 5DB2CE06
P 7850 5150
F 0 "#PWR?" H 7850 5000 50  0001 C CNN
F 1 "+5V" V 7865 5278 50  0000 L CNN
F 2 "" H 7850 5150 50  0001 C CNN
F 3 "" H 7850 5150 50  0001 C CNN
	1    7850 5150
	0    -1   -1   0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5DB2D73E
P 7850 4700
F 0 "#PWR?" H 7850 4550 50  0001 C CNN
F 1 "+BATT" V 7865 4827 50  0000 L CNN
F 2 "" H 7850 4700 50  0001 C CNN
F 3 "" H 7850 4700 50  0001 C CNN
	1    7850 4700
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8100 4700 7850 4700
Wire Wire Line
	7850 5150 8100 5150
$EndSCHEMATC
