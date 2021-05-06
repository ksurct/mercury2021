// encoderCurrentPosition, EncoderOldPosition, EncoderCurrentTime, EncoderOldTime, EncoderSpeed
int EncoderA[4];
int EncoderB[4];
int EncoderC[4];
int EncoderD[4];

#define EncoderTicks 420
#define Cirumfrence ((9.5/2)*PI*2) // wheel diameter is about 9.5cm
// single-channel output: 420 counts per main shaft revolution for 1:60 geared motor, 7 pulses per rear shaft revolution

void setup() {
  Serial.begin(9600);
  Serial.println("Basic Encoder Test:");
  //set up interrupts
  //back right (encoderA)
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  //back left (encoderB)
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  //front left (encoderC)
  pinMode(6, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
  //front right (encoderD)
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);
  // Interupts:
  attachInterrupt(digitalPinToInterrupt(2+1), EncoderMonitorA, RISING);
  attachInterrupt(digitalPinToInterrupt(4+1), EncoderMonitorB, RISING);
  attachInterrupt(digitalPinToInterrupt(6+1), EncoderMonitorC, RISING);
  attachInterrupt(digitalPinToInterrupt(8+1), EncoderMonitorD, RISING);
}

void loop() {
    Serial.print("EncoderAPos:");
    Serial.print(EncoderA[0]);
    Serial.print(", ");
    Serial.print("EncoderASpeed:");
    EncoderSpeedA();
    Serial.print(EncoderA[4]);
    Serial.print(", ");
    Serial.print("EncoderBPos:");
    Serial.print(EncoderB[0]);
    Serial.print(", ");
    Serial.print("EncoderBSpeed:");
    EncoderSpeedB();
    Serial.print(EncoderB[4]);
    Serial.print(", ");
    Serial.print("EncoderCPos:");
    Serial.print(EncoderC[0]);
    Serial.print(", ");
    Serial.print("EncoderCSpeed:");
    EncoderSpeedC();
    Serial.print(EncoderC[4]);
    Serial.print(", ");
    Serial.print("EncoderDPos:");
    Serial.print(EncoderD[0]);
    Serial.print(", ");
    Serial.print("EncoderDSpeed:");
    EncoderSpeedD();
    Serial.print(EncoderD[4]);
    Serial.print(", ");
    Serial.println(); // nice and semtrical now -ω-
}

void EncoderMonitorA() {
  if (digitalRead(2+1) == digitalRead(3+1)) { //if input A = input B...
    EncoderA[0]++; //add to the encoderPosition
  }
  else {
    EncoderA[0]--; //if not, subtract from the encoderPosition
  }
}

void EncoderMonitorB() {
  if (digitalRead(4+1) == digitalRead(5+1)) {
    EncoderB[0]++;
  }
  else {
    EncoderB[0]--;
  }
}

void EncoderMonitorC() {
  if (digitalRead(6+1) == digitalRead(7+1)) {
    EncoderC[0]++;
  }
  else {
    EncoderC[0]--;
  }
}

void EncoderMonitorD() {
  if (digitalRead(8+1) == digitalRead(9+1)) {
    EncoderD[0]++;
  }
  else {
    EncoderD[0]--;
  }
}
// encoderCurrentPosition, EncoderOldPosition, EncoderCurrentTime, EncoderOldTime, EncoderSpeed
void EncoderSpeedA() {
  EncoderA[2] = millis();
  EncoderA[4] = (((((((EncoderA[0]-EncoderA[1])/EncoderTicks)*Cirumfrence)/100)/(EncoderA[2]-EncoderA[3])));
  EncoderA[3] = EncoderA[2];
  EncoderA[1] = EncoderA[0];
  int DistanceA = 0;
}
void EncoderSpeedB() {
  EncoderB[2] = millis();
  EncoderB[4] = (((((((EncoderA[0]-EncoderA[1])/EncoderTicks)*Cirumfrence)/100)/(EncoderB[2]-EncoderB[3]))));
  EncoderB[3] = EncoderB[2];
  EncoderB[1] = EncoderB[0];
}
void EncoderSpeedC() {
  EncoderC[2] = millis();
  EncoderC[4] = (((((((EncoderA[0]-EncoderA[1])/EncoderTicks)*Cirumfrence)/100)/(EncoderC[2]-EncoderC[3]));
  EncoderC[3] = EncoderC[2];
  EncoderC[1] = EncoderC[0];
}
void EncoderSpeedD() {
  EncoderD[2] = millis();
  EncoderD[4] = ((((((EncoderA[0]-EncoderA[1])/EncoderTicks)*Cirumfrence)/100)/(EncoderD[2]-EncoderD[3]))/);
  EncoderD[3] = EncoderD[2];
  EncoderD[1] = EncoderD[0];
}
