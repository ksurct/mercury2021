EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 3
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
L Mercury:MDD10A U?
U 3 1 60981FBB
P 750 800
AR Path="/60981FBB" Ref="U?"  Part="3" 
AR Path="/6094441B/60981FBB" Ref="U?"  Part="3" 
AR Path="/60979A3C/60981FBB" Ref="U11"  Part="3" 
F 0 "U11" H 812 1075 50  0000 C CNN
F 1 "PCA9685" H 812 984 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 750 1000 50  0001 C CNN
F 3 "" H 750 1000 50  0001 C CNN
	3    750  800 
	1    0    0    -1  
$EndComp
$Comp
L Mercury:MDD10A U?
U 3 1 60981FCD
P 750 1750
AR Path="/60981FCD" Ref="U?"  Part="3" 
AR Path="/6094441B/60981FCD" Ref="U?"  Part="3" 
AR Path="/60979A3C/60981FCD" Ref="U13"  Part="3" 
F 0 "U13" H 812 2025 50  0000 C CNN
F 1 "PCA9685" H 812 1934 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 750 1950 50  0001 C CNN
F 3 "" H 750 1950 50  0001 C CNN
	3    750  1750
	1    0    0    -1  
$EndComp
$Comp
L Mercury:MDD10A U?
U 1 1 60981FD9
P 2800 1550
AR Path="/60981FD9" Ref="U?"  Part="1" 
AR Path="/6094441B/60981FD9" Ref="U?"  Part="1" 
AR Path="/60979A3C/60981FD9" Ref="U11"  Part="1" 
F 0 "U11" H 3119 1451 50  0000 L CNN
F 1 "PCA9685" H 3119 1360 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 2800 1750 50  0001 C CNN
F 3 "" H 2800 1750 50  0001 C CNN
	1    2800 1550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 1900 2550 1900
Wire Wire Line
	2700 1800 2550 1800
Wire Wire Line
	2700 1700 2550 1700
Wire Wire Line
	2700 1600 2550 1600
Wire Wire Line
	2700 1500 2550 1500
Entry Wire Line
	2550 1900 2450 1800
Entry Wire Line
	2550 1800 2450 1700
Entry Wire Line
	2550 1700 2450 1600
Entry Wire Line
	2550 1600 2450 1500
Entry Wire Line
	2550 1500 2450 1400
Text Label 2650 1900 2    50   ~ 0
RM_GND
Text Label 2650 1800 2    50   ~ 0
RM_PWM2_GPIO12
Text Label 2650 1700 2    50   ~ 0
RM_DIR2_GPIO21
Text Label 2650 1600 2    50   ~ 0
RM_PWM1_GPIO18
Text Label 2650 1500 2    50   ~ 0
RM_DIR1_GPIO20
$Comp
L Mercury:MDD10A U?
U 1 1 60981FEE
P 2800 2150
AR Path="/60981FEE" Ref="U?"  Part="1" 
AR Path="/6094441B/60981FEE" Ref="U?"  Part="1" 
AR Path="/60979A3C/60981FEE" Ref="U13"  Part="1" 
F 0 "U13" H 3119 2051 50  0000 L CNN
F 1 "PCA9685" H 3119 1960 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 2800 2350 50  0001 C CNN
F 3 "" H 2800 2350 50  0001 C CNN
	1    2800 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 2500 2550 2500
Wire Wire Line
	2700 2400 2550 2400
Wire Wire Line
	2700 2300 2550 2300
Wire Wire Line
	2700 2200 2550 2200
Wire Wire Line
	2700 2100 2550 2100
Entry Wire Line
	2550 2500 2450 2400
Entry Wire Line
	2550 2400 2450 2300
Entry Wire Line
	2550 2300 2450 2200
Entry Wire Line
	2550 2200 2450 2100
Entry Wire Line
	2550 2100 2450 2000
Text Label 2650 2100 2    50   ~ 0
LM_DIR1_GPIO6
Text Label 2650 2300 2    50   ~ 0
LM_DIR2_GPIO5
Text Label 2650 2200 2    50   ~ 0
LM_PWM1_GPIO19
Text Label 2650 2400 2    50   ~ 0
LM_PWM2_GPIO13
Text Label 2650 2500 2    50   ~ 0
LM_GND
Wire Bus Line
	2450 2250 1650 2250
Connection ~ 2450 2250
Wire Bus Line
	2450 1650 1650 1650
Connection ~ 2450 1650
Text Label 1700 1650 0    50   ~ 0
RightMotor
Text Label 1700 2250 0    50   ~ 0
LeftMotor
Entry Bus Bus
	1550 2350 1650 2250
Entry Bus Bus
	1550 1750 1650 1650
$Comp
L Connector:Raspberry_Pi_2_3 J?
U 1 1 60987481
P 6450 2200
AR Path="/60987481" Ref="J?"  Part="1" 
AR Path="/6094441B/60987481" Ref="J?"  Part="1" 
AR Path="/60979A3C/60987481" Ref="J15"  Part="1" 
F 0 "J15" H 6450 3681 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 6450 3590 50  0000 C CNN
F 2 "" H 6450 2200 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 6450 2200 50  0001 C CNN
	1    6450 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 1800 5450 1800
Wire Wire Line
	5650 2000 5450 2000
Wire Wire Line
	5650 2100 5450 2100
Wire Wire Line
	5650 2200 5450 2200
Entry Wire Line
	5300 1700 5400 1800
Entry Wire Line
	5350 1900 5450 2000
Entry Wire Line
	5350 2000 5450 2100
Entry Wire Line
	5350 2100 5450 2200
Wire Wire Line
	7250 2000 7450 2000
Wire Wire Line
	7250 2100 7450 2100
Wire Wire Line
	7250 2900 7450 2900
Wire Wire Line
	7250 3000 7450 3000
Entry Wire Line
	7450 2900 7550 2800
Entry Wire Line
	7550 2900 7450 3000
Entry Wire Line
	7550 1900 7450 2000
Entry Wire Line
	7550 2000 7450 2100
Entry Wire Line
	6050 3600 6150 3700
Wire Wire Line
	6050 3500 6050 3600
Text Label 7300 2100 0    50   ~ 0
LM_DIR1_GPIO6
Text Label 7300 2000 0    50   ~ 0
LM_DIR2_GPIO5
Text Label 5500 2000 2    50   ~ 0
LM_PWM1_GPIO19
Text Label 7300 3000 0    50   ~ 0
LM_PWM2_GPIO13
Text Label 6050 3550 3    50   ~ 0
LM_GND
Text Label 5450 1800 2    50   ~ 0
RM_PWM1_GPIO18
Text Label 5500 2100 2    50   ~ 0
RM_DIR1_GPIO20
Text Label 5500 2200 2    50   ~ 0
RM_DIR2_GPIO21
Text Label 7300 2900 0    50   ~ 0
RM_PWM2_GPIO12
Entry Wire Line
	6150 3600 6250 3700
Text Label 6150 3550 3    50   ~ 0
RM_GND
Wire Wire Line
	6150 3600 6150 3500
Connection ~ 5350 2800
Wire Bus Line
	5350 2800 5350 3700
$Comp
L Mercury:PCA9685 U12
U 2 1 609948C9
P 3800 1300
F 0 "U12" H 3969 950 50  0000 L CNN
F 1 "PCA9685" H 3969 859 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 3800 1500 50  0001 C CNN
F 3 "" H 3800 1500 50  0001 C CNN
	2    3800 1300
	-1   0    0    1   
$EndComp
Entry Wire Line
	3450 650  3350 750 
Entry Wire Line
	3450 750  3350 850 
Entry Wire Line
	3450 850  3350 950 
Entry Wire Line
	3450 950  3350 1050
Entry Wire Line
	3450 1050 3350 1150
Entry Wire Line
	3450 1150 3350 1250
Wire Bus Line
	3350 1400 3650 1400
Entry Bus Bus
	3650 2700 3750 2800
Wire Bus Line
	3650 1400 3650 2700
Wire Wire Line
	3600 650  3450 650 
Wire Wire Line
	3450 750  3600 750 
Wire Wire Line
	3600 850  3450 850 
Wire Wire Line
	3450 950  3600 950 
Wire Wire Line
	3600 1050 3450 1050
Wire Wire Line
	3450 1150 3600 1150
Entry Wire Line
	6250 3600 6350 3700
$Comp
L Mercury:PCA9685 U?
U 3 1 6098200C
P 750 1250
AR Path="/6098200C" Ref="U?"  Part="3" 
AR Path="/609567C6/6098200C" Ref="U?"  Part="3" 
AR Path="/60979A3C/6098200C" Ref="U12"  Part="3" 
F 0 "U12" H 880 1259 50  0000 L CNN
F 1 "PCA9685" H 880 1168 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 750 1450 50  0001 C CNN
F 3 "" H 750 1450 50  0001 C CNN
	3    750  1250
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6250 3500 6250 3600
Entry Wire Line
	7400 1600 7500 1500
Entry Wire Line
	7400 1700 7500 1600
Wire Bus Line
	7550 1550 7500 1550
Wire Bus Line
	7500 1500 7500 1550
Connection ~ 7500 1550
Wire Bus Line
	7500 1550 7500 1600
Wire Wire Line
	7250 1600 7400 1600
Wire Wire Line
	7400 1700 7250 1700
Text Label 3500 1150 2    50   ~ 0
Servo_CTL_GND
Text Label 6250 3550 3    50   ~ 0
Servo_GND_GND
Text Label 3500 1050 2    50   ~ 0
Servo_OE
Text Label 3500 950  2    50   ~ 0
Servo_SCL
Text Label 3500 850  2    50   ~ 0
Servo_SDA
Text Label 3500 750  2    50   ~ 0
Serco_VCC
Text Label 3500 650  2    50   ~ 0
Servo_V+
Text Label 7350 1600 0    50   ~ 0
Servo_SDA
Text Label 7350 1700 0    50   ~ 0
Servo_SCL
Entry Wire Line
	7550 3400 7650 3500
Entry Wire Line
	7550 3500 7650 3600
Entry Wire Line
	7550 3300 7650 3400
Wire Wire Line
	7650 3400 7800 3400
Wire Wire Line
	7650 3500 7800 3500
Wire Wire Line
	7650 3600 7800 3600
NoConn ~ 7800 3400
NoConn ~ 7800 3500
NoConn ~ 7800 3600
Text Label 7700 3400 0    50   ~ 0
Servo_CE
Text Label 7700 3500 0    50   ~ 0
Servo_V+
Text Label 7700 3600 0    50   ~ 0
Servo_VCC
Entry Wire Line
	1100 750  1200 850 
Entry Wire Line
	1100 850  1200 950 
Entry Wire Line
	1100 1200 1200 1300
Entry Wire Line
	1100 1300 1200 1400
Entry Wire Line
	1100 1700 1200 1800
Entry Wire Line
	1100 1800 1200 1900
Wire Wire Line
	950  750  1100 750 
Wire Wire Line
	950  850  1100 850 
Wire Wire Line
	950  1200 1100 1200
Wire Wire Line
	950  1300 1100 1300
Wire Wire Line
	950  1700 1100 1700
Wire Wire Line
	950  1800 1100 1800
Text Label 1000 750  0    50   ~ 0
RM_VIN
Text Label 1000 850  0    50   ~ 0
RM_GND
Text Label 1000 1200 0    50   ~ 0
Servo_GND
Text Label 1000 1300 0    50   ~ 0
Servo_VIN
Text Label 1000 1700 0    50   ~ 0
LM_VIN
Text Label 1000 1800 0    50   ~ 0
LM_GND
Text HLabel 1200 2100 0    50   Input ~ 0
MotorPower
$Comp
L Connector_Generic:Conn_02x03_Counter_Clockwise J22
U 1 1 609CB3BE
P 4650 800
F 0 "J22" H 4700 1117 50  0000 C CNN
F 1 "Conn_02x03_Counter_Clockwise" H 4700 1026 50  0000 C CNN
F 2 "" H 4650 800 50  0001 C CNN
F 3 "~" H 4650 800 50  0001 C CNN
	1    4650 800 
	1    0    0    -1  
$EndComp
$Comp
L Mercury:PCA9685 U12
U 4 1 609BDBFC
P 4550 800
F 0 "U12" H 4708 484 50  0000 L CNN
F 1 "PCA9685" H 4708 393 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 4550 1000 50  0001 C CNN
F 3 "" H 4550 1000 50  0001 C CNN
	4    4550 800 
	0    1    1    0   
$EndComp
$Comp
L Connector:Conn_01x06_Female J25
U 1 1 60A355DA
P 5400 2700
F 0 "J25" H 5292 2175 50  0000 C CNN
F 1 "Conn_01x06_Female" H 5292 2266 50  0000 C CNN
F 2 "" H 5400 2700 50  0001 C CNN
F 3 "~" H 5400 2700 50  0001 C CNN
	1    5400 2700
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x02_Female J24
U 1 1 60A36CF4
P 5400 1700
F 0 "J24" H 5292 1375 50  0000 C CNN
F 1 "Conn_01x02_Female" H 5292 1466 50  0000 C CNN
F 2 "" H 5400 1700 50  0001 C CNN
F 3 "~" H 5400 1700 50  0001 C CNN
	1    5400 1700
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x02_Female J23
U 1 1 60A3828A
P 5400 1400
F 0 "J23" H 5292 1075 50  0000 C CNN
F 1 "Conn_01x02_Female" H 5292 1166 50  0000 C CNN
F 2 "" H 5400 1400 50  0001 C CNN
F 3 "~" H 5400 1400 50  0001 C CNN
	1    5400 1400
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x05_Female J29
U 1 1 60A3B73C
P 7500 2500
F 0 "J29" H 7528 2526 50  0000 L CNN
F 1 "Conn_01x05_Female" H 7528 2435 50  0000 L CNN
F 2 "" H 7500 2500 50  0001 C CNN
F 3 "~" H 7500 2500 50  0001 C CNN
	1    7500 2500
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x05_Female J27
U 1 1 60A3C8AB
P 6550 3750
F 0 "J27" V 6396 3998 50  0000 L CNN
F 1 "Conn_01x05_Female" V 6487 3998 50  0000 L CNN
F 2 "" H 6550 3750 50  0001 C CNN
F 3 "~" H 6550 3750 50  0001 C CNN
	1    6550 3750
	0    1    1    0   
$EndComp
$Comp
L Connector:Conn_01x05_Female J26
U 1 1 60A3E5BD
P 6450 650
F 0 "J26" V 6388 362 50  0000 R CNN
F 1 "Conn_01x05_Female" V 6297 362 50  0000 R CNN
F 2 "" H 6450 650 50  0001 C CNN
F 3 "~" H 6450 650 50  0001 C CNN
	1    6450 650 
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Conn_01x03_Female J28
U 1 1 60AD4F38
P 7500 1400
F 0 "J28" H 7528 1426 50  0000 L CNN
F 1 "Conn_01x03_Female" H 7528 1335 50  0000 L CNN
F 2 "" H 7500 1400 50  0001 C CNN
F 3 "~" H 7500 1400 50  0001 C CNN
	1    7500 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	7250 1500 7300 1500
Wire Wire Line
	7250 1500 7250 1900
Wire Wire Line
	7250 1300 7300 1300
Wire Wire Line
	7300 1400 7250 1400
Text Label 7300 1300 0    50   ~ 0
Pi_GPIO00
Text Label 7300 1400 0    50   ~ 0
Pi_GPIO01
Text Label 7300 1500 0    50   ~ 0
Pi_GPIO04
Text Label 7300 2300 0    50   ~ 0
Pi_GPIO07
Text Label 7300 2400 0    50   ~ 0
Pi_GPIO08
Text Label 7300 2500 0    50   ~ 0
Pi_GPIO09
Text Label 7300 2600 0    50   ~ 0
Pi_GPIO10
Text Label 7300 2700 0    50   ~ 0
Pi_GPIO11
Text Label 5600 2400 0    50   ~ 0
Pi_GPIO22
Text Label 5600 2500 0    50   ~ 0
Pi_GPIO23
Text Label 5600 2600 0    50   ~ 0
Pi_GPIO24
Text Label 5600 2700 0    50   ~ 0
Pi_GPIO25
Text Label 5600 2800 0    50   ~ 0
Pi_GPIO26
Text Label 5600 2900 0    50   ~ 0
Pi_GPIO27
Text Label 5600 1300 0    50   ~ 0
Pi_GPIO14
Text Label 5600 1400 0    50   ~ 0
Pi_GPIO15
Text Label 5600 1600 0    50   ~ 0
Pi_GPIO16
Text Label 5600 1700 0    50   ~ 0
Pi_GPIO17
Wire Wire Line
	5650 1300 5600 1300
Wire Wire Line
	5600 1400 5650 1400
Wire Wire Line
	5650 1600 5600 1600
Wire Wire Line
	5600 1700 5650 1700
Wire Wire Line
	5650 2400 5600 2400
Wire Wire Line
	5600 2500 5650 2500
Wire Wire Line
	5650 2600 5600 2600
Wire Wire Line
	5600 2700 5650 2700
Wire Wire Line
	5650 2800 5600 2800
Wire Wire Line
	5600 2900 5650 2900
Wire Wire Line
	7300 2300 7250 2300
Wire Wire Line
	7250 2400 7300 2400
Wire Wire Line
	7300 2500 7250 2500
Wire Wire Line
	7250 2600 7300 2600
Wire Wire Line
	7300 2700 7250 2700
Wire Wire Line
	6750 3550 6750 3500
Wire Wire Line
	6650 3500 6650 3550
Wire Wire Line
	6550 3500 6550 3550
Wire Wire Line
	6450 3550 6450 3500
Wire Wire Line
	6350 3500 6350 3550
Text Label 6350 3550 1    50   ~ 0
Pi_GND
Text Label 6450 3550 1    50   ~ 0
Pi_GND
Text Label 6550 3550 1    50   ~ 0
Pi_GND
Text Label 6650 3550 1    50   ~ 0
Pi_GND
Text Label 6750 3550 1    50   ~ 0
Pi_GND
NoConn ~ 6450 850 
Text Label 6650 850  1    50   ~ 0
Pi_3v3
Text Label 6550 850  1    50   ~ 0
Pi_3v3
Text Label 6350 850  1    50   ~ 0
Pi_5v
Text Label 6250 850  1    50   ~ 0
Pi_5v
Wire Wire Line
	6650 850  6650 900 
Wire Wire Line
	6550 850  6550 900 
Wire Wire Line
	6350 850  6350 900 
Wire Wire Line
	6250 850  6250 900 
Wire Wire Line
	5000 700  4950 700 
Wire Wire Line
	4950 800  5000 800 
Wire Wire Line
	5000 900  4950 900 
Wire Wire Line
	4400 900  4450 900 
Wire Wire Line
	4450 800  4400 800 
Wire Wire Line
	4400 700  4450 700 
$Comp
L Mercury:PCA9685 U12
U 5 1 609BF816
P 5100 850
F 0 "U12" H 5258 534 50  0000 L CNN
F 1 "PCA9685" H 5258 443 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 5100 1050 50  0001 C CNN
F 3 "" H 5100 1050 50  0001 C CNN
	5    5100 850 
	0    1    1    0   
$EndComp
Wire Wire Line
	5000 700  5000 750 
Wire Wire Line
	5000 750  4950 750 
Wire Wire Line
	5000 800  5000 850 
Wire Wire Line
	5000 850  4950 850 
Wire Wire Line
	5000 900  5000 950 
Wire Wire Line
	5000 950  4950 950 
Wire Bus Line
	1550 2800 5350 2800
Wire Bus Line
	1550 1750 1550 2800
Wire Bus Line
	2450 2250 2450 2400
Wire Bus Line
	2450 1650 2450 1800
Wire Bus Line
	2450 1400 2450 1650
Wire Bus Line
	2450 2000 2450 2250
Wire Bus Line
	5350 3700 7550 3700
Wire Bus Line
	5350 1700 5350 2800
Wire Bus Line
	3350 750  3350 1400
Wire Bus Line
	7550 1550 7550 3700
Wire Bus Line
	1200 850  1200 2150
$EndSCHEMATC
