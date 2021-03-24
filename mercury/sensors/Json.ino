#include <ArduinoJson.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  StaticJsonDocument<200> doc;

  // Array of Encoders
  JsonArray encoder = doc.createNestedArray("encoder");
  encoder.add(1.234);
  encoder.add(5.678);
  encoder.add(8.765);
  encoder.add(4.321);

  // Array of Distance Sensors
  JsonArray dist = doc.createNestedArray("distance");
  dist.add(1);
  dist.add(2);
  dist.add(3);

  // Hall's Effect Sensor
  doc["magnet"] = 1.03;
}

void loop() {
  // put your main code here, to run repeatedly:

}
