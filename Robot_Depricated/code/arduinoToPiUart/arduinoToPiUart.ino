//#include <SoftwareSerial.h>
#include <Arduino.h>

//SoftwareSerial mySerial(2, 3); // RX, TX
void setup() {
  Serial.begin(9600);
  //while (!Serial) {
    
  //}

//  mySerial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
//  if (mySerial.available())
  Serial.write('H');
  //delay(20);
}
