#include "Adafruit_VL53L0X.h"
#include "Wire.h"

#define TCAADDR 0x70

#define SENSOR_NUM 2

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void tcaselect(uint8_t i) {
  if (i > 7) return;
 
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}

void setup() {
  Serial.begin(115200);
  Wire.begin();

  // wait until serial port opens for native USB devices
  while (! Serial) {
    delay(1);
  }
  
  Serial.println("Adafruit VL53L0X test");
  for(int i = 0; i < SENSOR_NUM; i++)
  {
    tcaselect(i);
    if (!lox.begin()) {
      Serial.print(F("Failed to boot VL53L0X at ")); Serial.println(i);
      while(1);
    }
    // power 
    Serial.print("Sensor ready at "); Serial.println(i); 
  }
}


void loop() {
  for(int i = 0; i < SENSOR_NUM; i++)
  {
    VL53L0X_RangingMeasurementData_t measure;
    tcaselect(i);   
    Serial.print("Sensor "); Serial.print(i); Serial.print(": ");
    lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
  
    if (measure.RangeStatus != 4) {  // phase failures have incorrect data
      Serial.println(measure.RangeMilliMeter);
    } else {
      Serial.println(" out of range ");
    }
  }   
   delay(100);
}
