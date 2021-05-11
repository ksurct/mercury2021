#include "Sensors.hpp"
#include "Json.hpp"
#include "Adafruit_VL53L0X.h"
#include "Wire.h"

#define TCAADDR 0x70


static Adafruit_VL53L0X lox = Adafruit_VL53L0X();
static bool initedSensors[json::Data::NUM_SENSORS];

void tcaselect(uint8_t i) {
  if (i > 7) return;
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}

void sensors::readSensors() {
    for(int i = 0; i < json::Data::NUM_SENSORS; i++)
    {
        if (!initedSensors[i]) {
            json::Data::data.sensors[i] = 0;
            return;
        }
        VL53L0X_RangingMeasurementData_t measure;
        tcaselect(i);   
        lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
    
        if (measure.RangeStatus != 4) {  // phase failures have incorrect data
            json::Data::data.sensors[i] = (measure.RangeMilliMeter);
        } else {
            json::Data::data.sensors[i] = 0;
        }
    }   
}

void sensors::initSensors() {
    memset(initedSensors, 0, json::Data::NUM_SENSORS);
    Wire.begin();

    // wait until serial port opens for native USB devices
    while (! Serial) {
        delay(1);
    }
    
    Serial.println("Initializing sensors");
    for(int i = 0; i < json::Data::NUM_SENSORS; i++)
    {
        tcaselect(i);
        if (!lox.begin()) {
            Serial.print(F("Failed to boot VL53L0X at ")); Serial.println(i);
        } else {
            // power 
            Serial.print("Sensor ready at "); Serial.println(i); 
            initedSensors[i] = true;
        }
    }
    Serial.println("Done Initializing sensors");
}