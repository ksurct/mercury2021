EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 4
Title "Mercury 2021 Motherboard"
Date "2021-04-14"
Rev "2.0 Alpha"
Comp "Kansas State University Robotics Competition Team"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 "https://github.com/ksurct/mercury2021/issues/10"
$EndDescr
$Comp
L power:+5V #PWR?
U 1 1 60EA5EEC
P 3200 4150
AR Path="/60EA5EEC" Ref="#PWR?"  Part="1" 
AR Path="/60E98AAB/60EA5EEC" Ref="#PWR0101"  Part="1" 
F 0 "#PWR0101" H 3200 4000 50  0001 C CNN
F 1 "+5V" H 3215 4323 50  0001 C CNN
F 2 "" H 3200 4150 50  0001 C CNN
F 3 "" H 3200 4150 50  0001 C CNN
	1    3200 4150
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 60EA5EF2
P 2900 3850
AR Path="/60EA5EF2" Ref="#PWR?"  Part="1" 
AR Path="/60E98AAB/60EA5EF2" Ref="#PWR0102"  Part="1" 
F 0 "#PWR0102" H 2900 3600 50  0001 C CNN
F 1 "GND" H 2905 3677 50  0001 C CNN
F 2 "" H 2900 3850 50  0001 C CNN
F 3 "" H 2900 3850 50  0001 C CNN
	1    2900 3850
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Linear:LM1084-5.0 U?
U 1 1 60EA5EF8
P 3200 3850
AR Path="/60EA5EF8" Ref="U?"  Part="1" 
AR Path="/60E98AAB/60EA5EF8" Ref="U1"  Part="1" 
F 0 "U1" V 3154 3955 50  0000 L CNN
F 1 "LM1084-5.0" V 3245 3955 50  0000 L CNN
F 2 "Mercury 2021:LM1084" H 3200 4100 50  0001 C CIN
F 3 "http://www.ti.com/lit/ds/symlink/lm1084.pdf" H 3200 3850 50  0001 C CNN
	1    3200 3850
	0    1    1    0   
$EndComp
Wire Wire Line
	3000 3550 2900 3550
Wire Wire Line
	3100 3550 3200 3550
Wire Wire Line
	2900 3550 2900 3850
Wire Wire Line
	2900 3850 3450 3850
Connection ~ 2900 3850
Connection ~ 3200 3550
Connection ~ 3200 4150
$Comp
L power:+BATT #PWR?
U 1 1 60EA5F06
P 3200 3550
AR Path="/60EA5F06" Ref="#PWR?"  Part="1" 
AR Path="/60E98AAB/60EA5F06" Ref="#PWR0103"  Part="1" 
F 0 "#PWR0103" H 3200 3400 50  0001 C CNN
F 1 "+BATT" H 3300 3650 50  0001 C CNN
F 2 "" H 3200 3550 50  0001 C CNN
F 3 "" H 3200 3550 50  0001 C CNN
	1    3200 3550
	1    0    0    -1  
$EndComp
Text Label 3750 3550 0    50   ~ 0
11.1V
Text Label 3750 3850 0    50   ~ 0
GND
Text Label 3750 4150 0    50   ~ 0
5V
$Comp
L Device:CP C?
U 1 1 60EA5F0F
P 3450 3700
AR Path="/60EA5F0F" Ref="C?"  Part="1" 
AR Path="/60E98AAB/60EA5F0F" Ref="C1"  Part="1" 
F 0 "C1" H 3568 3746 50  0000 L CNN
F 1 "10μf" H 3568 3655 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P2.50mm" H 3488 3550 50  0001 C CNN
F 3 "~" H 3450 3700 50  0001 C CNN
	1    3450 3700
	1    0    0    -1  
$EndComp
Connection ~ 3450 3550
Connection ~ 3450 3850
Wire Wire Line
	3450 3850 4050 3850
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA5F18
P 3000 3350
AR Path="/60EA5F18" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA5F18" Ref="J1"  Part="1" 
F 0 "J1" V 2964 3162 50  0001 R CNN
F 1 "Batt_Power" V 3150 3700 50  0000 R CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 3000 3350 50  0001 C CNN
F 3 "~" H 3000 3350 50  0001 C CNN
	1    3000 3350
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Conn_01x11_Male J?
U 1 1 60EA5F1E
P 4200 4750
AR Path="/60EA5F1E" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA5F1E" Ref="J7"  Part="1" 
F 0 "J7" H 4172 4682 50  0000 R CNN
F 1 "5V rail" H 4172 4773 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x11_P2.54mm_Vertical" H 4200 4750 50  0001 C CNN
F 3 "~" H 4200 4750 50  0001 C CNN
	1    4200 4750
	-1   0    0    1   
$EndComp
Wire Wire Line
	4000 4150 4000 4250
Wire Wire Line
	4000 4250 4000 4350
Connection ~ 4000 4250
Wire Wire Line
	4000 4350 4000 4450
Connection ~ 4000 4350
Connection ~ 4000 5250
Connection ~ 4000 4450
Wire Wire Line
	4000 4450 4000 4550
Connection ~ 4000 4550
Wire Wire Line
	4000 4550 4000 4650
Connection ~ 4000 4650
Wire Wire Line
	4000 4650 4000 4750
Connection ~ 4000 4750
Wire Wire Line
	4000 4750 4000 4850
Connection ~ 4000 4850
Wire Wire Line
	4000 4850 4000 4950
Connection ~ 4000 4950
Wire Wire Line
	4000 4950 4000 5050
Connection ~ 4000 5050
Wire Wire Line
	4000 5050 4000 5150
Connection ~ 4000 5150
Wire Wire Line
	4000 5150 4000 5250
$Comp
L Connector:Conn_01x11_Male J?
U 1 1 60EA5F3B
P 4700 4450
AR Path="/60EA5F3B" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA5F3B" Ref="J8"  Part="1" 
F 0 "J8" H 4672 4382 50  0000 R CNN
F 1 "GND Rail 1" V 4672 4473 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x11_P2.54mm_Vertical" H 4700 4450 50  0001 C CNN
F 3 "~" H 4700 4450 50  0001 C CNN
	1    4700 4450
	-1   0    0    1   
$EndComp
Wire Wire Line
	4500 3850 4500 3950
Wire Wire Line
	4500 3950 4500 4050
Connection ~ 4500 3950
Wire Wire Line
	4500 4050 4500 4150
Connection ~ 4500 4050
Connection ~ 4500 4150
Wire Wire Line
	4500 4150 4500 4250
Connection ~ 4500 4250
Wire Wire Line
	4500 4250 4500 4350
Connection ~ 4500 4350
Wire Wire Line
	4500 4350 4500 4450
Connection ~ 4500 4450
Wire Wire Line
	4500 4450 4500 4550
Connection ~ 4500 4550
Wire Wire Line
	4500 4550 4500 4650
Connection ~ 4500 4650
Wire Wire Line
	4500 4650 4500 4750
Connection ~ 4500 4750
Wire Wire Line
	4500 4750 4500 4850
Connection ~ 4500 4850
Wire Wire Line
	4500 4850 4500 4950
$Comp
L Connector:Conn_01x11_Male J?
U 1 1 60EA5F57
P 5200 4150
AR Path="/60EA5F57" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA5F57" Ref="J9"  Part="1" 
F 0 "J9" H 5172 4082 50  0000 R CNN
F 1 "11v rail" H 5172 4173 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x11_P2.54mm_Vertical" H 5200 4150 50  0001 C CNN
F 3 "~" H 5200 4150 50  0001 C CNN
	1    5200 4150
	-1   0    0    1   
$EndComp
Wire Wire Line
	5000 3550 5000 3650
Wire Wire Line
	5000 3650 5000 3750
Connection ~ 5000 3650
Wire Wire Line
	5000 3750 5000 3850
Connection ~ 5000 3750
Connection ~ 5000 4650
Connection ~ 5000 3850
Wire Wire Line
	5000 3850 5000 3950
Connection ~ 5000 3950
Wire Wire Line
	5000 3950 5000 4050
Connection ~ 5000 4050
Wire Wire Line
	5000 4050 5000 4150
Connection ~ 5000 4150
Wire Wire Line
	5000 4150 5000 4250
Connection ~ 5000 4250
Wire Wire Line
	5000 4250 5000 4350
Connection ~ 5000 4350
Wire Wire Line
	5000 4350 5000 4450
Connection ~ 5000 4450
Wire Wire Line
	5000 4450 5000 4550
Connection ~ 5000 4550
Wire Wire Line
	5000 4550 5000 4650
Wire Wire Line
	5000 4650 5000 4750
Wire Wire Line
	4000 6050 4200 6050
Text Label 4050 6050 0    50   ~ 0
Sense_VDD
Entry Wire Line
	4200 6050 4300 6150
Wire Bus Line
	4300 5900 4400 5900
Connection ~ 4300 5900
Wire Wire Line
	4000 6050 4000 6150
Wire Wire Line
	4000 6150 4200 6150
Connection ~ 4000 6050
Entry Wire Line
	4200 6150 4300 6250
Text Label 4050 6150 0    50   ~ 0
MP_+5V
Text Label 4750 5100 0    50   ~ 0
MP_GND
Entry Wire Line
	5150 4850 5250 4950
Entry Wire Line
	5150 4950 5250 5050
Wire Wire Line
	5000 4850 5150 4850
Wire Wire Line
	5000 4950 5150 4950
Wire Wire Line
	5000 4750 5150 4750
Text Label 5050 4850 0    50   ~ 0
RM_VIN
Text Label 5050 4950 0    50   ~ 0
Servo_VIN
Text Label 5050 4750 0    50   ~ 0
LM_VIN
Entry Wire Line
	5150 4750 5250 4850
Wire Wire Line
	4700 5100 4900 5100
Text Label 4750 5300 0    50   ~ 0
LM_GNDA
Text Label 4750 5200 0    50   ~ 0
Servo_GND
Entry Wire Line
	4900 5100 5000 5200
Wire Wire Line
	4700 5200 4900 5200
Wire Wire Line
	4700 5300 4900 5300
Wire Wire Line
	4700 5400 4900 5400
Wire Wire Line
	4700 5100 4700 5200
Connection ~ 4700 5200
Wire Wire Line
	4700 5200 4700 5300
Text Label 4750 5400 0    50   ~ 0
RM_GNDA
Wire Wire Line
	4700 5300 4700 5400
Connection ~ 4700 5300
Entry Wire Line
	4900 5200 5000 5300
Entry Wire Line
	4900 5300 5000 5400
Connection ~ 5000 4750
Wire Wire Line
	5000 4750 5000 4850
Wire Wire Line
	5000 4850 5000 4950
Connection ~ 5000 4850
Wire Bus Line
	4400 6400 4400 5900
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA5FEE
P 6050 3400
AR Path="/60EA5FEE" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA5FEE" Ref="J12"  Part="1" 
F 0 "J12" H 6130 3392 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 6130 3301 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 6050 3400 50  0001 C CNN
F 3 "~" H 6050 3400 50  0001 C CNN
	1    6050 3400
	0    1    1    0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA5FF4
P 6300 3400
AR Path="/60EA5FF4" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA5FF4" Ref="J14"  Part="1" 
F 0 "J14" H 6380 3392 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 6380 3301 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 6300 3400 50  0001 C CNN
F 3 "~" H 6300 3400 50  0001 C CNN
	1    6300 3400
	0    1    1    0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA5FFA
P 6550 3400
AR Path="/60EA5FFA" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA5FFA" Ref="J31"  Part="1" 
F 0 "J31" H 6630 3392 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 6630 3301 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 6550 3400 50  0001 C CNN
F 3 "~" H 6550 3400 50  0001 C CNN
	1    6550 3400
	0    1    1    0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA6000
P 6800 3400
AR Path="/60EA6000" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA6000" Ref="J33"  Part="1" 
F 0 "J33" H 6880 3392 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 6880 3301 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 6800 3400 50  0001 C CNN
F 3 "~" H 6800 3400 50  0001 C CNN
	1    6800 3400
	0    1    1    0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA6006
P 7050 3400
AR Path="/60EA6006" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA6006" Ref="J35"  Part="1" 
F 0 "J35" H 7130 3392 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 7130 3301 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 7050 3400 50  0001 C CNN
F 3 "~" H 7050 3400 50  0001 C CNN
	1    7050 3400
	0    1    1    0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA600C
P 6950 2100
AR Path="/60EA600C" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA600C" Ref="J34"  Part="1" 
F 0 "J34" H 6868 1775 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 6868 1866 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 6950 2100 50  0001 C CNN
F 3 "~" H 6950 2100 50  0001 C CNN
	1    6950 2100
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA6012
P 6700 2100
AR Path="/60EA6012" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA6012" Ref="J32"  Part="1" 
F 0 "J32" H 6618 1775 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 6618 1866 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 6700 2100 50  0001 C CNN
F 3 "~" H 6700 2100 50  0001 C CNN
	1    6700 2100
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA6018
P 6450 2100
AR Path="/60EA6018" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA6018" Ref="J30"  Part="1" 
F 0 "J30" H 6368 1775 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 6368 1866 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 6450 2100 50  0001 C CNN
F 3 "~" H 6450 2100 50  0001 C CNN
	1    6450 2100
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA601E
P 6200 2100
AR Path="/60EA601E" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA601E" Ref="J13"  Part="1" 
F 0 "J13" H 6118 1775 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 6118 1866 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 6200 2100 50  0001 C CNN
F 3 "~" H 6200 2100 50  0001 C CNN
	1    6200 2100
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA6024
P 5950 2100
AR Path="/60EA6024" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA6024" Ref="J11"  Part="1" 
F 0 "J11" H 5868 1775 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 5868 1866 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 5950 2100 50  0001 C CNN
F 3 "~" H 5950 2100 50  0001 C CNN
	1    5950 2100
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4000 4150 4150 4150
Wire Wire Line
	7050 2450 7050 2300
Connection ~ 4000 4150
Wire Wire Line
	6800 2300 6800 2450
Connection ~ 6800 2450
Wire Wire Line
	6800 2450 7050 2450
Wire Wire Line
	6550 2300 6550 2450
Connection ~ 6550 2450
Wire Wire Line
	6550 2450 6800 2450
Wire Wire Line
	6300 2300 6300 2450
Connection ~ 6300 2450
Wire Wire Line
	6300 2450 6550 2450
Wire Wire Line
	6050 2300 6050 2450
Connection ~ 6050 2450
Wire Wire Line
	6050 2450 6300 2450
Wire Wire Line
	6950 2800 6950 2300
Wire Wire Line
	6700 2300 6700 2800
Connection ~ 6700 2800
Wire Wire Line
	6700 2800 6950 2800
Wire Wire Line
	6450 2300 6450 2800
Connection ~ 6450 2800
Wire Wire Line
	6450 2800 6700 2800
Wire Wire Line
	6200 2300 6200 2800
Connection ~ 6200 2800
Wire Wire Line
	6200 2800 6450 2800
Wire Wire Line
	5950 2300 5950 2800
Connection ~ 5950 2800
Wire Wire Line
	5950 2800 6200 2800
Wire Wire Line
	7050 3100 7050 3200
Wire Wire Line
	6800 3100 6800 3200
Connection ~ 6800 3100
Wire Wire Line
	6800 3100 7050 3100
Wire Wire Line
	6550 3200 6550 3100
Connection ~ 6550 3100
Wire Wire Line
	6550 3100 6800 3100
Wire Wire Line
	6300 3200 6300 3100
Connection ~ 6300 3100
Wire Wire Line
	6300 3100 6550 3100
Wire Wire Line
	6050 3200 6050 3100
Connection ~ 6050 3100
Wire Wire Line
	6050 3100 6300 3100
Wire Wire Line
	6950 2800 6950 3200
Connection ~ 6950 2800
Wire Wire Line
	6700 2800 6700 3200
Wire Wire Line
	6450 2800 6450 3200
Wire Wire Line
	6200 2800 6200 3200
Wire Wire Line
	5950 2800 5950 3200
$Comp
L Device:CP C?
U 1 1 60EA605F
P 3450 4000
AR Path="/60EA605F" Ref="C?"  Part="1" 
AR Path="/60E98AAB/60EA605F" Ref="C2"  Part="1" 
F 0 "C2" H 3332 3954 50  0000 R CNN
F 1 "10μf" H 3332 4045 50  0000 R CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P2.50mm" H 3488 3850 50  0001 C CNN
F 3 "~" H 3450 4000 50  0001 C CNN
	1    3450 4000
	-1   0    0    1   
$EndComp
Wire Wire Line
	3450 3550 3700 3550
$Comp
L Device:CP C?
U 1 1 60EA6068
P 3700 3400
AR Path="/60EA6068" Ref="C?"  Part="1" 
AR Path="/60E98AAB/60EA6068" Ref="C4"  Part="1" 
F 0 "C4" H 3582 3354 50  0000 R CNN
F 1 "10μf" H 3582 3445 50  0000 R CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P2.50mm" H 3738 3250 50  0001 C CNN
F 3 "~" H 3700 3400 50  0001 C CNN
	1    3700 3400
	-1   0    0    1   
$EndComp
$Comp
L Device:CP C?
U 1 1 60EA606E
P 3700 3100
AR Path="/60EA606E" Ref="C?"  Part="1" 
AR Path="/60E98AAB/60EA606E" Ref="C3"  Part="1" 
F 0 "C3" H 3818 3146 50  0000 L CNN
F 1 "10μf" H 3818 3055 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P2.50mm" H 3738 2950 50  0001 C CNN
F 3 "~" H 3700 3100 50  0001 C CNN
	1    3700 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	3200 4150 3450 4150
Connection ~ 3450 4150
Wire Wire Line
	3450 4150 4000 4150
Connection ~ 3700 3550
Wire Wire Line
	3700 3550 4600 3550
Wire Wire Line
	3350 2950 3700 2950
Connection ~ 3700 2950
Connection ~ 5350 3650
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA60A0
P 3700 1750
AR Path="/60EA60A0" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA60A0" Ref="J2"  Part="1" 
F 0 "J2" H 3618 1425 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 3618 1516 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 3700 1750 50  0001 C CNN
F 3 "~" H 3700 1750 50  0001 C CNN
	1    3700 1750
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA60A6
P 3700 2000
AR Path="/60EA60A6" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA60A6" Ref="J3"  Part="1" 
F 0 "J3" H 3618 1675 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 3618 1766 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 3700 2000 50  0001 C CNN
F 3 "~" H 3700 2000 50  0001 C CNN
	1    3700 2000
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA60AC
P 3700 2250
AR Path="/60EA60AC" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA60AC" Ref="J4"  Part="1" 
F 0 "J4" H 3618 1925 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 3618 2016 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 3700 2250 50  0001 C CNN
F 3 "~" H 3700 2250 50  0001 C CNN
	1    3700 2250
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA60B2
P 3700 2500
AR Path="/60EA60B2" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA60B2" Ref="J5"  Part="1" 
F 0 "J5" H 3618 2175 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 3618 2266 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 3700 2500 50  0001 C CNN
F 3 "~" H 3700 2500 50  0001 C CNN
	1    3700 2500
	-1   0    0    1   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 60EA60B8
P 3700 2750
AR Path="/60EA60B8" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA60B8" Ref="J6"  Part="1" 
F 0 "J6" H 3618 2425 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 3618 2516 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 3700 2750 50  0001 C CNN
F 3 "~" H 3700 2750 50  0001 C CNN
	1    3700 2750
	-1   0    0    1   
$EndComp
Wire Wire Line
	4050 1650 3900 1650
Wire Wire Line
	3900 1900 4050 1900
Connection ~ 4050 1900
Wire Wire Line
	4050 1900 4050 1650
Wire Wire Line
	3900 2150 4050 2150
Connection ~ 4050 2150
Wire Wire Line
	4050 2150 4050 1900
Wire Wire Line
	3900 2400 4050 2400
Connection ~ 4050 2400
Wire Wire Line
	4050 2400 4050 2150
Wire Wire Line
	3900 2650 4050 2650
Connection ~ 4050 2650
Wire Wire Line
	4050 2650 4050 2400
Wire Wire Line
	4400 1750 3900 1750
Wire Wire Line
	3900 2000 4400 2000
Connection ~ 4400 2000
Wire Wire Line
	4400 2000 4400 1750
Wire Wire Line
	3900 2250 4400 2250
Connection ~ 4400 2250
Wire Wire Line
	4400 2250 4400 2000
Wire Wire Line
	3900 2500 4400 2500
Connection ~ 4400 2500
Wire Wire Line
	4400 2500 4400 2250
Wire Wire Line
	3900 2750 4400 2750
Connection ~ 4400 2750
Wire Wire Line
	4400 2750 4400 2500
Wire Wire Line
	4400 2750 4400 2950
Connection ~ 4400 2950
Connection ~ 4050 3850
Wire Wire Line
	3700 2950 4400 2950
Wire Wire Line
	4050 2650 4050 3850
Wire Wire Line
	4050 3850 4500 3850
Wire Wire Line
	4500 2800 4500 3850
Wire Wire Line
	4500 2800 5950 2800
Connection ~ 4500 3850
Wire Wire Line
	4600 2450 6050 2450
Wire Wire Line
	4000 3100 4000 4150
Wire Wire Line
	4000 3100 6050 3100
Text HLabel 4400 6350 0    50   Input ~ 0
PowerBus
Wire Wire Line
	3200 3550 3450 3550
Entry Wire Line
	4300 5750 4200 5650
Text Label 4200 5650 2    50   ~ 0
Arduino_3v3
Connection ~ 4600 3550
Wire Wire Line
	4600 3550 5000 3550
Wire Wire Line
	4400 2950 5350 2950
Wire Wire Line
	4600 2450 4600 3550
Wire Wire Line
	5350 2950 5350 3350
Wire Wire Line
	5350 4350 5350 4450
Wire Wire Line
	5350 4250 5350 4350
Connection ~ 5350 4250
Connection ~ 5350 4150
Wire Wire Line
	5350 4150 5350 4250
Wire Wire Line
	5350 4050 5350 4150
Connection ~ 5350 4050
Connection ~ 5350 3950
Wire Wire Line
	5350 3950 5350 4050
Wire Wire Line
	5350 3850 5350 3950
Connection ~ 5350 3850
Connection ~ 5350 3750
Wire Wire Line
	5350 3750 5350 3850
Wire Wire Line
	5350 3650 5350 3750
Wire Wire Line
	5350 3550 5350 3650
Connection ~ 5350 3550
Connection ~ 5350 4350
Connection ~ 5350 3450
Connection ~ 5350 3350
Wire Wire Line
	5350 3450 5350 3550
Wire Wire Line
	5350 3350 5350 3450
$Comp
L Connector:Conn_01x11_Male J?
U 1 1 60EA6082
P 5550 3850
AR Path="/60EA6082" Ref="J?"  Part="1" 
AR Path="/60E98AAB/60EA6082" Ref="J10"  Part="1" 
F 0 "J10" H 5522 3782 50  0000 R CNN
F 1 "3.3v rail" H 5522 3873 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x11_P2.54mm_Vertical" H 5550 3850 50  0001 C CNN
F 3 "~" H 5550 3850 50  0001 C CNN
	1    5550 3850
	-1   0    0    1   
$EndComp
Wire Wire Line
	4700 5850 4700 5750
Connection ~ 4700 5850
Wire Wire Line
	4700 5950 4700 5850
$Comp
L Connector:Conn_01x11_Male J?
U 1 1 61038F3E
P 4500 6150
AR Path="/61038F3E" Ref="J?"  Part="1" 
AR Path="/60E98AAB/61038F3E" Ref="J37"  Part="1" 
F 0 "J37" H 4472 6082 50  0000 R CNN
F 1 "GND rail 3" H 4900 5550 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x11_P2.54mm_Vertical" H 4500 6150 50  0001 C CNN
F 3 "~" H 4500 6150 50  0001 C CNN
	1    4500 6150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4700 6550 4700 6650
Connection ~ 4700 6550
Wire Wire Line
	4700 6450 4700 6550
Connection ~ 4700 6450
Wire Wire Line
	4700 6350 4700 6450
Connection ~ 4700 6350
Wire Wire Line
	4700 6250 4700 6350
Connection ~ 4700 6250
Wire Wire Line
	4700 6150 4700 6250
Connection ~ 4700 6150
Wire Wire Line
	4700 6050 4700 6150
Connection ~ 4700 6050
Wire Wire Line
	4700 5950 4700 6050
Connection ~ 4700 5950
Connection ~ 4700 6650
Connection ~ 4700 5750
Connection ~ 4700 5650
Wire Wire Line
	4700 5650 4700 5750
$Comp
L Connector:Conn_01x11_Male J?
U 1 1 6102E3C8
P 4900 6150
AR Path="/6102E3C8" Ref="J?"  Part="1" 
AR Path="/60E98AAB/6102E3C8" Ref="J36"  Part="1" 
F 0 "J36" H 4872 6082 50  0000 R CNN
F 1 "GND rail 2" V 4872 6173 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x11_P2.54mm_Vertical" H 4900 6150 50  0001 C CNN
F 3 "~" H 4900 6150 50  0001 C CNN
	1    4900 6150
	-1   0    0    1   
$EndComp
Entry Wire Line
	4900 5400 5000 5500
Wire Wire Line
	4500 4950 4500 5050
Wire Wire Line
	4500 5050 4550 5050
Wire Wire Line
	4700 5050 4700 5100
Connection ~ 4500 4950
Connection ~ 4700 5100
Wire Bus Line
	5000 5500 5150 5500
Connection ~ 5250 5500
Entry Wire Line
	4900 5500 5000 5600
Wire Bus Line
	5000 5500 5000 5600
Connection ~ 5000 5500
Wire Wire Line
	4900 5500 4700 5500
Wire Wire Line
	4700 5500 4700 5650
Text Label 4750 5500 0    50   ~ 0
Sense_GND
Wire Wire Line
	4700 5500 4700 5400
Connection ~ 4700 5500
Connection ~ 4700 5400
Wire Bus Line
	4300 5000 5150 5000
Wire Bus Line
	5150 5000 5150 5500
Wire Bus Line
	5250 5500 5250 5900
Connection ~ 5150 5500
Wire Bus Line
	5150 5500 5250 5500
Wire Wire Line
	3350 5650 4200 5650
Wire Wire Line
	3350 2950 3350 5650
Text GLabel 4750 5100 2    50   Input ~ 0
MP_GND
Text GLabel 4750 5200 2    50   Input ~ 0
SERVO_GND
Text GLabel 4750 5300 2    50   Input ~ 0
LM_GND_MAIN
Text GLabel 4750 5500 2    50   Input ~ 0
Sense_GND
Text GLabel 4800 5400 2    50   Input ~ 0
RM_GND_MAIN
Text GLabel 5050 4750 2    50   Input ~ 0
LM_VIN
Text GLabel 5050 4850 2    50   Input ~ 0
RM_VIN
Text GLabel 5050 4950 2    50   Input ~ 0
SERVO_VIN
Text GLabel 4100 6050 2    50   Input ~ 0
Sense_VDD
Text GLabel 4050 6150 2    50   Input ~ 0
MP_5v
Wire Wire Line
	4000 5250 4000 5500
Text GLabel 4100 5650 2    50   Input ~ 0
Arduino_3v3
Text GLabel 4100 5500 2    50   Input ~ 0
Pi_5v
Text GLabel 4450 5300 3    50   Input ~ 0
Pi_GND
Entry Wire Line
	4300 5200 4400 5300
Entry Wire Line
	4300 5400 4200 5500
Wire Wire Line
	4200 5500 4000 5500
Connection ~ 4000 5500
Wire Wire Line
	4000 5500 4000 6050
Wire Wire Line
	4550 5050 4550 5300
Wire Wire Line
	4550 5300 4400 5300
Wire Bus Line
	4300 5900 4300 6250
Wire Bus Line
	5250 4850 5250 5500
Wire Bus Line
	5000 5200 5000 5500
Wire Bus Line
	4300 5000 4300 5900
Connection ~ 4550 5050
Wire Wire Line
	4550 5050 4700 5050
$EndSCHEMATC
