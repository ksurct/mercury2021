// encoderCurrentPosition, EncoderOldPosition, EncoderCurrentTime, EncoderOldTime, EncoderSpeed
float EncoderA[5];
float EncoderB[5];
float EncoderC[5];
float EncoderD[5];

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
// single-channel output: 420 counts per main shaft revolution for 1:60 geared motor, 7 pulses per rear shaft revolution

void setup() {
  Serial.begin(9600);
//  Serial.println("Basic Encoder Test:");
  //set up interrupts
  //back right (encoderA)
  pinMode(EncoderA1, INPUT_PULLUP);
  pinMode(EncoderA2, INPUT_PULLUP);
  //back left (encoderB)
  pinMode(EncoderB1, INPUT_PULLUP);
  pinMode(EncoderB2, INPUT_PULLUP);
  //front left (encoderC)
  pinMode(EncoderC1, INPUT_PULLUP);
  pinMode(EncoderC2, INPUT_PULLUP);
  //front right (encoderD)
  pinMode(EncoderD1, INPUT_PULLUP);
  pinMode(EncoderD2, INPUT_PULLUP);
  // Interupts:
  attachInterrupt(digitalPinToInterrupt(EncoderA1), EncoderMonitorA, RISING);
  attachInterrupt(digitalPinToInterrupt(EncoderB1), EncoderMonitorB, RISING);
  attachInterrupt(digitalPinToInterrupt(EncoderC1), EncoderMonitorC, RISING);
  attachInterrupt(digitalPinToInterrupt(EncoderD1), EncoderMonitorD, RISING);
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
// encoderCurrentPosition, EncoderOldPosition, EncoderCurrentTime, EncoderOldTime, EncoderSpeed
//   Change in ticks = (EncoderX[0]-EncoderX[1])
//   Rotations = (Change in ticks)/EncoderTicks
//   Change in distance = Rotations*Cirumfrence
//   Change in time = (EncoderX[2]-EncoderX[4])
//   Speed = Change in distance/Change in time
  
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
