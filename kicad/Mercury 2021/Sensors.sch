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
AR Path="/6095675A/60963CE8" Ref="U?"  Part="1" 
F 0 "U?" H 7800 3581 50  0000 C CNN
F 1 "TCA9548APWR" H 7800 3490 50  0000 C CNN
F 2 "Package_SO:TSSOP-24_4.4x7.8mm_P0.65mm" H 7800 1500 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tca9548a.pdf" H 7850 2750 50  0001 C CNN
	1    7800 2500
	0    -1   -1   0   
$EndComp
$Comp
L MCU_Module:Arduino_Nano_Every A?
U 1 1 60963CEE
P 9150 5000
AR Path="/60963CEE" Ref="A?"  Part="1" 
AR Path="/6095675A/60963CEE" Ref="A?"  Part="1" 
F 0 "A?" H 9150 3911 50  0000 C CNN
F 1 "Arduino_Nano_Every" H 9150 3820 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 9150 5000 50  0001 C CIN
F 3 "https://content.arduino.cc/assets/NANOEveryV3.0_sch.pdf" H 9150 5000 50  0001 C CNN
	1    9150 5000
	-1   0    0    1   
$EndComp
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60963D0C
P 1600 1050
AR Path="/60963D0C" Ref="U?"  Part="1" 
AR Path="/6095675A/60963D0C" Ref="U?"  Part="1" 
F 0 "U?" V 2067 1050 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 1976 1050 50  0000 C CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 2275 500 50  0001 C CNN
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
NoConn ~ 1400 1450
NoConn ~ 1900 1450
NoConn ~ 2200 950 
NoConn ~ 1000 950 
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
AR Path="/6095675A/60A3405B" Ref="U?"  Part="1" 
F 0 "U?" V 3467 1050 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 3376 1050 50  0000 C CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 3675 500 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 3100 1050 50  0001 C CNN
	1    3000 1050
	0    -1   -1   0   
$EndComp
NoConn ~ 2800 1450
NoConn ~ 3300 1450
NoConn ~ 3600 950 
NoConn ~ 2400 950 
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
AR Path="/6095675A/60A34B37" Ref="U?"  Part="1" 
F 0 "U?" V 4867 1050 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 4776 1050 50  0000 C CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 5075 500 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 4500 1050 50  0001 C CNN
	1    4400 1050
	0    -1   -1   0   
$EndComp
NoConn ~ 4200 1450
NoConn ~ 4700 1450
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
AR Path="/6095675A/60A359AE" Ref="U?"  Part="1" 
F 0 "U?" V 6267 1050 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 6176 1050 50  0000 C CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 6475 500 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 5900 1050 50  0001 C CNN
	1    5800 1050
	0    -1   -1   0   
$EndComp
NoConn ~ 5600 1450
NoConn ~ 6100 1450
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
AR Path="/6095675A/60A8DDD9" Ref="U?"  Part="1" 
F 0 "U?" V 6117 2250 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 6026 2250 50  0000 C CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 6325 1700 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 5750 2250 50  0001 C CNN
	1    5650 2250
	0    1    1    0   
$EndComp
NoConn ~ 5850 1850
NoConn ~ 5350 1850
NoConn ~ 5050 2350
NoConn ~ 6250 2350
Entry Wire Line
	5650 1750 5550 1650
Entry Wire Line
	5550 1750 5450 1650
Wire Wire Line
	5550 1850 5550 1750
Wire Wire Line
	5650 1850 5650 1750
Text Label 5650 1800 1    50   ~ 0
SDA7
Text Label 5550 1800 1    50   ~ 0
SCL7
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60A8DDE9
P 4250 2250
AR Path="/60A8DDE9" Ref="U?"  Part="1" 
AR Path="/6095675A/60A8DDE9" Ref="U?"  Part="1" 
F 0 "U?" V 4717 2250 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 4626 2250 50  0000 C CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 4925 1700 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 4350 2250 50  0001 C CNN
	1    4250 2250
	0    1    1    0   
$EndComp
NoConn ~ 4450 1850
NoConn ~ 3950 1850
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
AR Path="/6095675A/60A8DDF9" Ref="U?"  Part="1" 
F 0 "U?" V 3317 2250 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 3226 2250 50  0000 C CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 3525 1700 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 2950 2250 50  0001 C CNN
	1    2850 2250
	0    1    1    0   
$EndComp
NoConn ~ 3050 1850
NoConn ~ 2550 1850
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
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 60A8DE09
P 1450 2250
AR Path="/60A8DE09" Ref="U?"  Part="1" 
AR Path="/6095675A/60A8DE09" Ref="U?"  Part="1" 
F 0 "U?" V 1917 2250 50  0000 C CNN
F 1 "VL53L1CXV0FY1" V 1826 2250 50  0000 C CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 2125 1700 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 1550 2250 50  0001 C CNN
	1    1450 2250
	0    1    1    0   
$EndComp
NoConn ~ 1650 1850
NoConn ~ 1150 1850
NoConn ~ 850  2350
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
	3600 2250 3650 2250
Wire Wire Line
	4850 2250 4900 2250
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
	8450 4500 8550 4600
Entry Wire Line
	8450 4400 8550 4500
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
Wire Wire Line
	8550 4600 8650 4600
Wire Wire Line
	8650 4500 8550 4500
Wire Bus Line
	7150 4350 8450 4350
Text Label 8600 4500 2    50   ~ 0
SCL
Text Label 8600 4600 2    50   ~ 0
SDA
Wire Bus Line
	9000 1850 9000 3100
Wire Bus Line
	8450 4350 8450 4500
Wire Bus Line
	7200 3100 9000 3100
Wire Bus Line
	6700 1850 9000 1850
Wire Bus Line
	700  1650 6700 1650
$EndSCHEMATC
