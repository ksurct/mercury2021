// encoderCurrentPosition, EncoderOldPosition, EncoderCurrentTime, EncoderOldTime, EncoderSpeed
int array EncoderA[5]
int array EncoderB[5]
int array EncoderC[5]
int array EncoderD[5]

#define int EncoderTicks = 420;
// single-channel output: 420 counts per main shaft revolution for 1:60 geared motor, 7 pulses per rear shaft revolution

void setup() {
  Serial.begin(9600);
  Serial.println("Basic Encoder Test:");
  //set up interrupts
  //back right (encoderA)
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  //back left (encoderB)
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  //front left (encoderC)
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  //front right (encoderD)
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  // Interupts:
  attachInterrupt(digitalPinToInterrupt(2), EncoderMonitorA, CHANGE);
  attachInterrupt(digitalPinToInterrupt(4), EncoderMonitorB, CHANGE);
  attachInterrupt(digitalPinToInterrupt(6), EncoderMonitorC, CHANGE);
  attachInterrupt(digitalPinToInterrupt(8), EncoderMonitorD, CHANGE);
}

void loop() {
    Serial.print("EncoderAPos:");
    Serial.print(EncoderA[0]);
    Serial.print(", ");
    Serial.print("EncoderASpeed:");
    Serial.print(EncoderA[4]);
    Serial.print(", ");
    Serial.print("EncoderBPos:");
    Serial.print(EncoderB[0]);
    Serial.print(", ");
    Serial.print("EncoderBSpeed:");
    Serial.print(EncoderB[4]);
    Serial.print(", ");
    Serial.print("EncoderCPos:");
    Serial.print(EncoderC[0]);
    Serial.print(", ");
    Serial.print("EncoderASpeed:");
    Serial.print(EncoderC[4]);
    Serial.print(", ");
    Serial.print("EncoderDPos:");
    Serial.print(EncoderD[0]);
    Serial.print(", ");
    Serial.print("EncoderASpeed:");
    Serial.print(EncoderD[4]);
    Serial.print(", ");
    Serial.println(); // nice and semtrical now -ω-
}

void EncoderMonitorA() {
  if (digitalRead(2) == digitalRead(3)) { //if input A = input B...
    EncoderA[0]++; //add to the encoderPosition
  }
  else {
    EncoderA[0]--; //if not, subtract from the encoderPosition
  }
}

void EncoderMonitorB() {
  if (digitalRead(4) == digitalRead(5)) {
    EncoderB[0]++;
  }
  else {
    EncoderB[0]--;
  }
}

void EncoderMonitorC() {
  if (digitalRead(6) == digitalRead(7)) {
    EncoderC[0]++;
  }
  else {
    EncoderC[0]--;
  }
}

void EncoderMonitorD() {
  if (digitalRead(8) == digitalRead(9)) {
    EncoderD[0]++;
  }
  else {
    EncoderD[0]--;
  }
}
// encoderCurrentPosition, EncoderOldPosition, EncoderCurrentTime, EncoderOldTime, EncoderSpeed
int EncoderSpeedA() {
  EncoderA[2] = millis();
  EncoderA[4] = (((((EncoderA[0]-EncoderA[1])*1000.0)/(EncoderA[2]-EncoderA[3]))*(2.0*PI))/EncoderTicks);
}
int EncoderSpeedB() {
  EncoderA[2] = millis();
  EncoderA[4] = (((((EncoderA[0]-EncoderA[1])*1000.0)/(EncoderA[2]-EncoderA[3]))*(2.0*PI))/EncoderTicks);
}
int EncoderSpeedC() {
  EncoderA[2] = millis();
  EncoderA[4] = (((((EncoderA[0]-EncoderA[1])*1000.0)/(EncoderA[2]-EncoderA[3]))*(2.0*PI))/EncoderTicks);
}
int EncoderSpeedD() {
  EncoderA[2] = millis();
  EncoderA[4] = (((((EncoderA[0]-EncoderA[1])*1000.0)/(EncoderA[2]-EncoderA[3]))*(2.0*PI))/EncoderTicks);
}
