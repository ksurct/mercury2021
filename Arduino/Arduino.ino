// encoderCurrentPosition, EncoderOldPosition, EncoderCurrentTime, EncoderOldTime, EncoderSpeed
float EncoderA[5];
float EncoderB[5];
float EncoderC[5];
float EncoderD[5];
boolean trigger;

String json;
#define HallEffect A0
#define EncoderA1 3   // RR
#define EncoderA2 4   // RR
#define EncoderB1 5   // RL
#define EncoderB2 6   // RL
#define EncoderC1 7   // FL
#define EncoderC2 8   // FL
#define EncoderD1 9   // FR
#define EncoderD2 10  // FR

#define EncoderTicks 420
float Circumference = ((9.5*100/2)*PI*2); // wheel diameter is about 9.5cm
#include "Adafruit_VL53L0X.h"
#include "Wire.h"

#define TCAADDR 0x70

#define SENSOR_NUM 2

void setup() {
  Serial.begin(115200);
  pinMode(EncoderA1, INPUT_PULLUP);
  pinMode(EncoderA2, INPUT_PULLUP);
  pinMode(EncoderB1, INPUT_PULLUP);
  pinMode(EncoderB2, INPUT_PULLUP);
  pinMode(EncoderC1, INPUT_PULLUP);
  pinMode(EncoderC2, INPUT_PULLUP);
  pinMode(EncoderD1, INPUT_PULLUP);
  pinMode(EncoderD2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(EncoderA1), EncoderMonitorA, RISING);
  attachInterrupt(digitalPinToInterrupt(EncoderB1), EncoderMonitorB, RISING);
  attachInterrupt(digitalPinToInterrupt(EncoderC1), EncoderMonitorC, RISING);
  attachInterrupt(digitalPinToInterrupt(EncoderD1), EncoderMonitorD, RISING);
  Wire.begin();
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

// GOAL: "{\"Encoders:\" \{\"Encoder A: \"EncoderA[4]\","Encoder B: \"EncoderB[4]\", "Encoder C: \"EncoderC[4]\", "Encoder D: \"EncoderD[4]\",\"\}}"
void loop(){
  analogRead(HallEffect);
  EncoderSpeedA();
  EncoderSpeedB();
  EncoderSpeedC();
  EncoderSpeedD();


  // for(int i = 0; i < SENSOR_NUM; i++)
  // {
  //   VL53L0X_RangingMeasurementData_t measure;
  //   tcaselect(i);
  //   Serial.print("Sensor "); Serial.print(i); Serial.print(": ");
  //   lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
  //
  //   if (measure.RangeStatus != 4) {  // phase failures have incorrect data
  //     Serial.println(measure.RangeMilliMeter);
  //   } else {
  //     Serial.println(" out of range ");
  //   }
  // }
  if(trigger)
  {
    Serial.println(json);
  }
  else{
    trigger = "";
  }
}


void EncoderMonitorA() {
  if (digitalRead(EncoderA1) == digitalRead(EncoderA2)) { //if input A = input B...
    EncoderA[0]++; //add to the encoderPosition
  }
  else {
    EncoderA[0]--; //if not, subtract from the encoderPosition
  }
}
void EncoderMonitorB() {
  if (digitalRead(EncoderB1) == digitalRead(EncoderB2)) {
    EncoderB[0]++;
  }
  else {
    EncoderB[0]--;
  }
}
void EncoderMonitorC() {
  if (digitalRead(EncoderC1) == digitalRead(EncoderC2)) {
    EncoderC[0]++;
  }
  else {
    EncoderC[0]--;
  }
}
void EncoderMonitorD() {
  if (digitalRead(EncoderD1) == digitalRead(EncoderD2)) {
    EncoderD[0]++;
  }
  else {
    EncoderD[0]--;
  }
}
void EncoderSpeedA() {
  EncoderA[2] = millis();
  EncoderA[4] = (((((EncoderA[0]-EncoderA[1])/EncoderTicks)*Circumference ))/(EncoderA[2]-EncoderA[3]));
  EncoderA[3] = EncoderA[2];
  EncoderA[1] = EncoderA[0];
}
void EncoderSpeedB() {
  EncoderB[2] = millis();
  EncoderB[4] = (((((EncoderB[0]-EncoderB[1])/EncoderTicks)*Circumference))/(EncoderB[2]-EncoderB[3]));
  EncoderB[3] = EncoderB[2];
  EncoderB[1] = EncoderB[0];
}
void EncoderSpeedC() {
  EncoderC[2] = millis();
  EncoderC[4] = (((((EncoderC[0]-EncoderC[1])/EncoderTicks)*Circumference ))/(EncoderC[2]-EncoderC[3]));
  EncoderC[3] = EncoderC[2];
  EncoderC[1] = EncoderC[0];
}
void EncoderSpeedD() {
  EncoderD[2] = millis();
  EncoderD[4] = (((((EncoderD[0]-EncoderD[1])/EncoderTicks)*Circumference ))/(EncoderD[2]-EncoderD[3]));
  EncoderD[3] = EncoderD[2];
  EncoderD[1] = EncoderD[0];
}

void tcaselect(uint8_t i) {
  if (i > 7) return;

  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();
}
