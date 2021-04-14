EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 3
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
L Interface_Expansion:TCA9548APWR U?
U 1 1 60963CE8
P 7800 2500
AR Path="/60963CE8" Ref="U?"  Part="1" 
AR Path="/6095675A/60963CE8" Ref="U10"  Part="1" 
F 0 "U10" H 7800 3581 50  0000 C CNN
F 1 "TCA9548APWR" H 7800 3490 50  0000 C CNN
F 2 "Package_SO:TSSOP-24_4.4x7.8mm_P0.65mm" H 7800 1500 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tca9548a.pdf" H 7850 2750 50  0001 C CNN
	1    7800 2500
	0    -1   -1   0   
$EndComp
$Comp
L MCU_Module:Arduino_Nano_Every A?
U 1 1 60963CEE
P 7000 4000
AR Path="/60963CEE" Ref="A?"  Part="1" 
AR Path="/6095675A/60963CEE" Ref="A1"  Part="1" 
F 0 "A1" H 7000 2911 50  0000 C CNN
F 1 "Arduino_Nano_Every" H 7000 2820 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 7000 4000 50  0001 C CIN
F 3 "https://content.arduino.cc/assets/NANOEveryV3.0_sch.pdf" H 7000 4000 50  0001 C CNN
	1    7000 4000
	0    -1   -1   0   
$EndComp
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60963D0C
P 1600 1050
AR Path="/60963D0C" Ref="U?"  Part="1" 
AR Path="/6095675A/60963D0C" Ref="U3"  Part="1" 
F 0 "U3" V 2067 1050 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 1976 1050 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 2275 500 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 1700 1050 50  0001 C CNN
	1    1600 1050
	0    -1   -1   0   
$EndComp
Entry Wire Line
	8500 1850 8600 1950
Wire Wire Line
	8600 1950 8600 2100
Entry Wire Line
	8400 1850 8500 1950
Wire Wire Line
	8500 1950 8500 2100
Entry Wire Line
	8300 1850 8400 1950
Wire Wire Line
	8400 1950 8400 2100
Entry Wire Line
	8200 1850 8300 1950
Wire Wire Line
	8300 1950 8300 2100
Entry Wire Line
	8100 1850 8200 1950
Wire Wire Line
	8200 1950 8200 2100
Entry Wire Line
	8000 1850 8100 1950
Wire Wire Line
	8100 1950 8100 2100
Entry Wire Line
	7900 1850 8000 1950
Wire Wire Line
	8000 1950 8000 2100
Entry Wire Line
	7800 1850 7900 1950
Wire Wire Line
	7900 1950 7900 2100
Entry Wire Line
	7700 1850 7800 1950
Wire Wire Line
	7800 1950 7800 2100
Entry Wire Line
	7600 1850 7700 1950
Wire Wire Line
	7700 1950 7700 2100
Entry Wire Line
	7500 1850 7600 1950
Wire Wire Line
	7600 1950 7600 2100
Entry Wire Line
	7400 1850 7500 1950
Wire Wire Line
	7500 1950 7500 2100
Entry Wire Line
	7300 1850 7400 1950
Wire Wire Line
	7400 1950 7400 2100
Entry Wire Line
	7200 1850 7300 1950
Wire Wire Line
	7300 1950 7300 2100
Entry Wire Line
	7100 1850 7200 1950
Wire Wire Line
	7200 1950 7200 2100
Entry Wire Line
	7000 1850 7100 1950
Wire Wire Line
	7100 1950 7100 2100
Entry Wire Line
	1600 1550 1700 1650
Entry Wire Line
	1700 1550 1800 1650
Wire Wire Line
	1700 1450 1700 1550
Wire Wire Line
	1600 1450 1600 1550
Text Label 1600 1500 3    50   ~ 0
SDA0
Text Label 1700 1500 3    50   ~ 0
SCL0
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60A3405B
P 3000 1050
AR Path="/60A3405B" Ref="U?"  Part="1" 
AR Path="/6095675A/60A3405B" Ref="U5"  Part="1" 
F 0 "U5" V 3467 1050 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 3376 1050 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 3675 500 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 3100 1050 50  0001 C CNN
	1    3000 1050
	0    -1   -1   0   
$EndComp
Entry Wire Line
	3000 1550 3100 1650
Entry Wire Line
	3100 1550 3200 1650
Wire Wire Line
	3100 1450 3100 1550
Wire Wire Line
	3000 1450 3000 1550
Text Label 3000 1500 3    50   ~ 0
SDA1
Text Label 3100 1500 3    50   ~ 0
SCL1
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60A34B37
P 4400 1050
AR Path="/60A34B37" Ref="U?"  Part="1" 
AR Path="/6095675A/60A34B37" Ref="U7"  Part="1" 
F 0 "U7" V 4867 1050 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 4776 1050 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 5075 500 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 4500 1050 50  0001 C CNN
	1    4400 1050
	0    -1   -1   0   
$EndComp
NoConn ~ 5000 950 
NoConn ~ 3800 950 
Entry Wire Line
	4400 1550 4500 1650
Entry Wire Line
	4500 1550 4600 1650
Wire Wire Line
	4500 1450 4500 1550
Wire Wire Line
	4400 1450 4400 1550
Text Label 4500 1500 3    50   ~ 0
SCL2
Text Label 4400 1500 3    50   ~ 0
SDA2
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60A359AE
P 5800 1050
AR Path="/60A359AE" Ref="U?"  Part="1" 
AR Path="/6095675A/60A359AE" Ref="U9"  Part="1" 
F 0 "U9" V 6267 1050 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 6176 1050 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 6475 500 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 5900 1050 50  0001 C CNN
	1    5800 1050
	0    -1   -1   0   
$EndComp
NoConn ~ 6400 950 
Entry Wire Line
	5800 1550 5900 1650
Entry Wire Line
	5900 1550 6000 1650
Wire Wire Line
	5900 1450 5900 1550
Wire Wire Line
	5800 1450 5800 1550
Text Label 5900 1500 3    50   ~ 0
SCL3
Text Label 5800 1500 3    50   ~ 0
SDA3
Wire Wire Line
	950  1550 950  1050
Wire Wire Line
	2250 1550 2250 1050
Wire Wire Line
	2350 1550 2350 1050
Wire Wire Line
	3650 1550 3650 1050
Wire Wire Line
	5050 1550 5050 1050
Wire Wire Line
	5150 1550 5150 1050
Wire Wire Line
	6450 1550 6450 1050
Entry Wire Line
	6450 1550 6550 1650
Entry Wire Line
	5150 1550 5250 1650
Entry Wire Line
	5050 1550 5150 1650
Entry Wire Line
	2350 1550 2450 1650
Entry Wire Line
	2250 1550 2350 1650
Entry Wire Line
	950  1550 1050 1650
Entry Wire Line
	3650 1550 3750 1650
Entry Wire Line
	3750 1550 3850 1650
Wire Wire Line
	3750 1550 3750 1050
Wire Wire Line
	6400 1050 6450 1050
Wire Wire Line
	5200 1050 5150 1050
Wire Wire Line
	5050 1050 5000 1050
Wire Wire Line
	3800 1050 3750 1050
Wire Wire Line
	3650 1050 3600 1050
Wire Wire Line
	2400 1050 2350 1050
Wire Wire Line
	2250 1050 2200 1050
Wire Wire Line
	1000 1050 950  1050
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60A8DDD9
P 5650 2250
AR Path="/60A8DDD9" Ref="U?"  Part="1" 
AR Path="/6095675A/60A8DDD9" Ref="U8"  Part="1" 
F 0 "U8" V 6117 2250 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 6026 2250 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 6325 1700 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 5750 2250 50  0001 C CNN
	1    5650 2250
	0    1    1    0   
$EndComp
NoConn ~ 5050 2350
NoConn ~ 6250 2350
Entry Wire Line
	5650 1750 5550 1650
Entry Wire Line
	5550 1750 5450 1650
Text Label 5650 1800 1    50   ~ 0
SDA7
Text Label 5550 1800 1    50   ~ 0
SCL7
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60A8DDE9
P 4250 2250
AR Path="/60A8DDE9" Ref="U?"  Part="1" 
AR Path="/6095675A/60A8DDE9" Ref="U6"  Part="1" 
F 0 "U6" V 4717 2250 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 4626 2250 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 4925 1700 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 4350 2250 50  0001 C CNN
	1    4250 2250
	0    1    1    0   
$EndComp
NoConn ~ 3650 2350
NoConn ~ 4850 2350
Entry Wire Line
	4250 1750 4150 1650
Entry Wire Line
	4150 1750 4050 1650
Wire Wire Line
	4150 1850 4150 1750
Wire Wire Line
	4250 1850 4250 1750
Text Label 4250 1800 1    50   ~ 0
SDA6
Text Label 4150 1800 1    50   ~ 0
SCL6
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60A8DDF9
P 2850 2250
AR Path="/60A8DDF9" Ref="U?"  Part="1" 
AR Path="/6095675A/60A8DDF9" Ref="U4"  Part="1" 
F 0 "U4" V 3317 2250 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 3226 2250 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 3525 1700 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 2950 2250 50  0001 C CNN
	1    2850 2250
	0    1    1    0   
$EndComp
NoConn ~ 2250 2350
NoConn ~ 3450 2350
Entry Wire Line
	2850 1750 2750 1650
Entry Wire Line
	2750 1750 2650 1650
Wire Wire Line
	2750 1850 2750 1750
Wire Wire Line
	2850 1850 2850 1750
Text Label 2750 1800 1    50   ~ 0
SCL5
Text Label 2850 1800 1    50   ~ 0
SDA5
Entry Wire Line
	1450 1750 1350 1650
Entry Wire Line
	1350 1750 1250 1650
Wire Wire Line
	1350 1850 1350 1750
Wire Wire Line
	1450 1850 1450 1750
Text Label 1350 1800 1    50   ~ 0
SCL4
Text Label 1450 1800 1    50   ~ 0
SDA4
Wire Wire Line
	6300 1750 6300 2250
Wire Wire Line
	5000 1750 5000 2250
Wire Wire Line
	4900 1750 4900 2250
Wire Wire Line
	3600 1750 3600 2250
Wire Wire Line
	2200 1750 2200 2250
Wire Wire Line
	2100 1750 2100 2250
Wire Wire Line
	800  1750 800  2250
Entry Wire Line
	800  1750 700  1650
Entry Wire Line
	2100 1750 2000 1650
Entry Wire Line
	2200 1750 2100 1650
Entry Wire Line
	4900 1750 4800 1650
Entry Wire Line
	5000 1750 4900 1650
Entry Wire Line
	6300 1750 6200 1650
Entry Wire Line
	3600 1750 3500 1650
Entry Wire Line
	3500 1750 3400 1650
Wire Wire Line
	3500 1750 3500 2250
Wire Wire Line
	850  2250 800  2250
Wire Wire Line
	2050 2250 2100 2250
Wire Wire Line
	2200 2250 2250 2250
Wire Wire Line
	3450 2250 3500 2250
Wire Wire Line
	5000 2250 5050 2250
Wire Wire Line
	6250 2250 6300 2250
Wire Bus Line
	6700 1650 6700 1850
Entry Wire Line
	6800 1850 6900 1950
Wire Wire Line
	6900 2500 6900 1950
Text Label 8600 2100 1    50   ~ 0
SDA7
Text Label 8500 2100 1    50   ~ 0
SCL7
Text Label 8400 2100 1    50   ~ 0
SDA6
Text Label 8300 2100 1    50   ~ 0
SCL6
Text Label 8200 2100 1    50   ~ 0
SDA5
Text Label 8100 2100 1    50   ~ 0
SCL5
Text Label 8000 2100 1    50   ~ 0
SDA4
Text Label 7900 2100 1    50   ~ 0
SCL4
Text Label 7800 2100 1    50   ~ 0
SDA3
Text Label 7700 2100 1    50   ~ 0
SCL3
Text Label 7600 2100 1    50   ~ 0
SDA2
Text Label 7500 2100 1    50   ~ 0
SCL2
Text Label 7400 2100 1    50   ~ 0
SDA1
Text Label 7300 2100 1    50   ~ 0
SCL1
Text Label 7200 2100 1    50   ~ 0
SDA0
Text Label 7100 2100 1    50   ~ 0
SCL0
Entry Wire Line
	8700 1850 8800 1950
Wire Wire Line
	8800 2500 8800 1950
Entry Wire Line
	7550 3100 7450 3200
Entry Wire Line
	7650 3100 7550 3200
Entry Wire Line
	7100 3000 7200 3100
Entry Wire Line
	7200 3000 7300 3100
Wire Wire Line
	7100 2900 7100 3000
Wire Wire Line
	7200 2900 7200 3000
Text Label 7100 2950 3    50   ~ 0
SCL
Text Label 7200 2950 3    50   ~ 0
SDA
Text Label 7550 3250 1    50   ~ 0
SCL
Text Label 7450 3250 1    50   ~ 0
SDA
Wire Bus Line
	9000 1850 9000 3100
Text Label 6900 2450 1    50   ~ 0
MP_+5V
Text Label 8800 2400 1    50   ~ 0
MP_GND
Text Label 950  1250 1    50   ~ 0
VDD0
Text Label 2250 1250 1    50   ~ 0
GND0
Text Label 2350 1250 1    50   ~ 0
VDD1
Text Label 3650 1250 1    50   ~ 0
GND1
Text Label 3750 1250 1    50   ~ 0
VDD2
Text Label 5050 1250 1    50   ~ 0
GND2
Text Label 5150 1250 1    50   ~ 0
VDD3
Text Label 6450 1250 1    50   ~ 0
GND3
Text Label 800  2250 1    50   ~ 0
GND5
Text Label 2100 2200 1    50   ~ 0
VDD5
Text Label 2200 2200 1    50   ~ 0
GND6
Text Label 3500 2200 1    50   ~ 0
VDD6
Text Label 3600 2200 1    50   ~ 0
GND7
Text Label 4900 2150 1    50   ~ 0
VDD7
Text Label 5000 2150 1    50   ~ 0
GND8
Text Label 6300 2150 1    50   ~ 0
VDD8
Wire Bus Line
	9000 3100 9000 3500
Connection ~ 9000 3100
Text HLabel 9000 3500 0    50   Input ~ 0
SensorPower
Wire Wire Line
	8300 2950 8300 2900
Wire Wire Line
	8200 2900 8200 2950
Wire Wire Line
	8100 2900 8100 2950
Text Label 8100 2950 1    50   ~ 0
MP_A2
Text Label 8200 2950 1    50   ~ 0
MP_A1
Text Label 8300 2950 1    50   ~ 0
MP_A0
Wire Wire Line
	7450 3500 7400 3500
Wire Wire Line
	7450 3200 7450 3500
Wire Wire Line
	7550 3500 7500 3500
Wire Wire Line
	7550 3200 7550 3500
Wire Wire Line
	7600 3450 7600 3500
Wire Wire Line
	7700 3450 7700 3500
Wire Wire Line
	7300 3450 7300 3500
Wire Wire Line
	7200 3450 7200 3500
Wire Wire Line
	7100 3450 7100 3500
Wire Wire Line
	7000 3500 7000 3450
NoConn ~ 7400 3450
NoConn ~ 7500 3450
$Comp
L Connector:Conn_01x09_Female J19
U 1 1 60A2ECF8
P 6900 4750
F 0 "J19" V 6973 4730 50  0000 C CNN
F 1 "Conn_01x09_Female" V 7064 4730 50  0000 C CNN
F 2 "" H 6900 4750 50  0001 C CNN
F 3 "~" H 6900 4750 50  0001 C CNN
	1    6900 4750
	0    1    1    0   
$EndComp
Wire Wire Line
	7300 4550 7300 4500
Wire Wire Line
	7200 4500 7200 4550
Wire Wire Line
	7100 4550 7100 4500
Wire Wire Line
	7000 4500 7000 4550
Wire Wire Line
	6900 4550 6900 4500
Wire Wire Line
	6800 4500 6800 4550
Wire Wire Line
	6700 4550 6700 4500
Wire Wire Line
	6600 4500 6600 4550
Wire Wire Line
	6500 4500 6500 4550
Wire Wire Line
	6300 4550 6300 4500
Wire Wire Line
	6200 4500 6200 4550
$Comp
L Connector:Conn_01x08_Female J20
U 1 1 609F4823
P 7300 3250
F 0 "J20" V 7465 3180 50  0000 C CNN
F 1 "Conn_01x08_Female" V 7374 3180 50  0000 C CNN
F 2 "" H 7300 3250 50  0001 C CNN
F 3 "~" H 7300 3250 50  0001 C CNN
	1    7300 3250
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6800 3500 6800 3450
Wire Wire Line
	6800 3450 6650 3450
Wire Wire Line
	6650 3450 6650 4200
Text Label 7000 3450 1    50   ~ 0
Arduino_A0
Text Label 7100 3450 1    50   ~ 0
Arduino_A1
Text Label 7200 3450 1    50   ~ 0
Arduino_A2
Text Label 7300 3450 1    50   ~ 0
Arduino_A3
Text Label 7400 3450 1    50   ~ 0
NC
Text Label 7500 3450 1    50   ~ 0
NC
Text Label 7700 3450 1    50   ~ 0
Arduino_A8
Text Label 7600 3450 1    50   ~ 0
Arduino_A7
Wire Wire Line
	6000 3800 5950 3800
Wire Wire Line
	5950 3900 6000 3900
Wire Wire Line
	5950 4000 8000 4000
Wire Wire Line
	5950 4100 6000 4100
Text Label 5950 4100 0    50   ~ 0
Arduino_VIN
Text Label 5950 4000 0    50   ~ 0
Arduino_GND
Text Label 5950 3900 0    50   ~ 0
Arduino_3v3
Text Label 5950 3800 0    50   ~ 0
Arduino_5v
NoConn ~ 7700 4500
NoConn ~ 7600 4500
NoConn ~ 7500 4500
NoConn ~ 6500 3500
Wire Wire Line
	6400 3500 6050 3500
Wire Wire Line
	6050 3500 6050 3700
Wire Wire Line
	6050 3700 5950 3700
Text Label 5950 3700 0    50   ~ 0
Arduino_Reset
Text Label 6200 4550 1    50   ~ 0
Arduino_Tx
Text Label 6300 4550 1    50   ~ 0
Arduino_Rx
$Comp
L Connector:Conn_01x06_Female J17
U 1 1 60AC219D
P 5750 4000
F 0 "J17" H 5642 3475 50  0000 C CNN
F 1 "Conn_01x06_Female" H 5642 3566 50  0000 C CNN
F 2 "" H 5750 4000 50  0001 C CNN
F 3 "~" H 5750 4000 50  0001 C CNN
	1    5750 4000
	-1   0    0    1   
$EndComp
Wire Wire Line
	5950 4200 6650 4200
Text Label 5950 4200 0    50   ~ 0
Arduino_AREF
$Comp
L Connector:Conn_01x02_Female J18
U 1 1 60AC80A7
P 6300 4750
F 0 "J18" V 6146 4798 50  0000 L CNN
F 1 "Conn_01x02_Female" V 6237 4798 50  0000 L CNN
F 2 "" H 6300 4750 50  0001 C CNN
F 3 "~" H 6300 4750 50  0001 C CNN
	1    6300 4750
	0    1    1    0   
$EndComp
Text Label 6500 4550 1    50   ~ 0
Arduino_D2
Text Label 6600 4550 1    50   ~ 0
Arduino_D3
Text Label 6700 4550 1    50   ~ 0
Arduino_D4
Text Label 6800 4550 1    50   ~ 0
Arduino_D5
Text Label 6900 4550 1    50   ~ 0
Arduino_D6
Text Label 7000 4550 1    50   ~ 0
Arduino_D7
Text Label 7100 4550 1    50   ~ 0
Arduino_D8
Text Label 7200 4550 1    50   ~ 0
Arduino_D9
Text Label 7300 4550 1    50   ~ 0
Arduino_D10
$Comp
L Connector:Conn_01x04_Female J21
U 1 1 60ACAFE3
P 8200 3150
F 0 "J21" V 8046 3298 50  0000 L CNN
F 1 "Conn_01x04_Female" V 8137 3298 50  0000 L CNN
F 2 "" H 8200 3150 50  0001 C CNN
F 3 "~" H 8200 3150 50  0001 C CNN
	1    8200 3150
	0    1    1    0   
$EndComp
Wire Wire Line
	8000 2950 8000 2900
Wire Wire Line
	8000 2900 7600 2900
Text Label 8000 2950 1    50   ~ 0
MP_Reset
NoConn ~ 3600 950 
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60A8DE09
P 1450 2250
AR Path="/60A8DE09" Ref="U?"  Part="1" 
AR Path="/6095675A/60A8DE09" Ref="U2"  Part="1" 
F 0 "U2" V 1917 2250 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 1826 2250 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 2125 1700 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 1550 2250 50  0001 C CNN
	1    1450 2250
	0    1    1    0   
$EndComp
NoConn ~ 2050 2350
NoConn ~ 850  2350
NoConn ~ 5200 950 
$Comp
L Connector:Conn_01x16_Female J16
U 1 1 60BF8EA2
P 3550 3200
F 0 "J16" V 3623 3130 50  0000 C CNN
F 1 "Conn_01x16_Female" V 3714 3130 50  0000 C CNN
F 2 "" H 3550 3200 50  0001 C CNN
F 3 "~" H 3550 3200 50  0001 C CNN
	1    3550 3200
	0    1    1    0   
$EndComp
Wire Wire Line
	1400 2900 2750 2900
Wire Wire Line
	1900 2850 2850 2850
Wire Wire Line
	2800 1450 2800 2750
Wire Wire Line
	2800 2750 2950 2750
Wire Wire Line
	3300 1450 3300 2250
Wire Wire Line
	3300 2250 3050 2250
Wire Wire Line
	4200 1450 3900 1450
Wire Wire Line
	3900 2650 3150 2650
Wire Wire Line
	4700 1450 4700 2300
Wire Wire Line
	4700 2300 3250 2300
Wire Wire Line
	5600 1450 4850 1450
Wire Wire Line
	4850 1450 4850 1600
Wire Wire Line
	4850 1600 4650 1600
Wire Wire Line
	4850 2250 4900 2250
Wire Wire Line
	3600 2250 3650 2250
Wire Wire Line
	5650 1850 5650 1750
Wire Wire Line
	5550 1850 5550 1750
Wire Wire Line
	4650 1600 4650 2200
Wire Wire Line
	6100 1450 6100 1700
Wire Wire Line
	6100 1700 4350 1700
Wire Wire Line
	4350 1700 4350 2500
Wire Wire Line
	4350 2500 3450 2500
Wire Wire Line
	5350 1850 5350 2900
Wire Wire Line
	5350 2900 4250 2900
Wire Wire Line
	5850 1850 5850 2850
Wire Wire Line
	5850 2850 4150 2850
Wire Wire Line
	4450 1850 4450 2800
Wire Wire Line
	4450 2800 3950 2800
Wire Wire Line
	3950 1850 3950 2750
Wire Wire Line
	3950 2750 4050 2750
Wire Wire Line
	3050 1850 3800 1850
Wire Wire Line
	3800 2750 3750 2750
Wire Wire Line
	3800 1850 3800 2750
Wire Wire Line
	2550 1850 2550 2450
Wire Wire Line
	2550 2450 3850 2450
Wire Wire Line
	3550 2700 1650 2700
Wire Wire Line
	1650 2700 1650 1850
Wire Wire Line
	1150 1850 1150 2600
Wire Wire Line
	1150 2600 3650 2600
NoConn ~ 2400 950 
NoConn ~ 1000 950 
NoConn ~ 2200 950 
Wire Wire Line
	1900 1450 1900 2850
Wire Wire Line
	1400 1450 1400 2900
Wire Wire Line
	4250 2900 4250 3000
Wire Wire Line
	4150 2850 4150 3000
Wire Wire Line
	4050 2750 4050 3000
Wire Wire Line
	3950 2800 3950 3000
Wire Wire Line
	3650 2600 3650 3000
Wire Wire Line
	3550 2700 3550 3000
Wire Wire Line
	3450 2500 3450 3000
Wire Wire Line
	3150 2650 3150 3000
Wire Wire Line
	3050 2250 3050 3000
Wire Wire Line
	2950 2750 2950 3000
Wire Wire Line
	2850 2850 2850 3000
Wire Wire Line
	2750 2900 2750 3000
Text Label 4250 2950 1    50   ~ 0
Sense7_XShut
Wire Wire Line
	3750 2750 3750 3000
Wire Wire Line
	3250 2300 3250 3000
Wire Wire Line
	3350 2550 3350 3000
Text Label 4150 2950 1    50   ~ 0
Sense7_GPIO
Text Label 4050 2950 1    50   ~ 0
Sense6_XShut
Wire Wire Line
	3900 1450 3900 2650
Wire Wire Line
	3850 2450 3850 3000
Text Label 3850 2950 1    50   ~ 0
Sense5_XShut
Text Label 3650 2950 1    50   ~ 0
Sense4_XShut
Text Label 3450 2950 1    50   ~ 0
Sense3_XShut
Text Label 3250 2900 1    50   ~ 0
Sense2_XShut
Text Label 3050 2900 1    50   ~ 0
Sense1_XShut
Text Label 2850 2950 1    50   ~ 0
Sense0_XShut
Text Label 2750 2950 1    50   ~ 0
Sense0_GPIO
Text Label 2950 2950 1    50   ~ 0
Sense1_GPIO
Text Label 3150 2950 1    50   ~ 0
Sense2_GPIO
Text Label 3350 2950 1    50   ~ 0
Sense3_GPIO
Text Label 3550 2950 1    50   ~ 0
Sense4_GPIO
Text Label 3750 2950 1    50   ~ 0
Sense5_GPIO
Text Label 3950 2950 1    50   ~ 0
Sense6_GPIO
Wire Wire Line
	3700 2200 3700 2550
Wire Wire Line
	3700 2200 4650 2200
Wire Bus Line
	7200 3100 9000 3100
Wire Bus Line
	6700 1850 9000 1850
Wire Bus Line
	700  1650 6700 1650
Wire Wire Line
	3700 2550 3350 2550
$EndSCHEMATC
