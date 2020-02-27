#include <SoftwareSerial.h>
int on = 0;
int in = 0;
//SoftwareSerial mySerial(2, 3); // RX, TX
void setup() {
  Serial.begin(9600, SERIAL_8O1);
  while (! Serial) {
    
  }

//  mySerial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
//  if (mySerial.available())
  Serial.write('H');
  //delay(20);
  if (0 || Serial.available()) {
    char x = Serial.read();
    Serial.write(x);
    if (x == '9') {
      Serial.write("It was 9\n");
      signal();
    }   
  }
}

void signal() {
  digitalWrite(2, HIGH);
  delay(1000);
  digitalWrite(2, LOW);
}
