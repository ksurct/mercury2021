
volatile int encoderPositionA;
volatile int encoderPositionB;
volatile int encoderPositionC;
volatile int encoderPositionD;

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
  attachInterrupt(digitalPinToInterrupt(2), EncoderMonitorA, CHANGE);
  attachInterrupt(digitalPinToInterrupt(4), EncoderMonitorB, CHANGE);
  attachInterrupt(digitalPinToInterrupt(6), EncoderMonitorC, CHANGE);
  attachInterrupt(digitalPinToInterrupt(8), EncoderMonitorD, CHANGE);
}

void loop() {
    Serial.print(encoderPositionA);
    Serial.print(encoderPositionB);
    Serial.print(encoderPositionC);
    Serial.println(encoderPositionD);
}

void EncoderMonitorA() {
  if (digitalRead(2) == digitalRead(3)) { //if input A = input B...
    encoderPositionA++; //add to the encoderPosition
  }
  else {
    encoderPositionA--; //if not, subtract from the encoderPosition
  }
}

void EncoderMonitorB() {
  if (digitalRead(4) == digitalRead(5)) {
    encoderPositionB++;
  }
  else {
    encoderPositionB--;
  }
}

void EncoderMonitorC() {
  if (digitalRead(6) == digitalRead(7)) {
    encoderPositionC++;
  }
  else {
    encoderPositionC--;
  }
}

void EncoderMonitorD() {
  if (digitalRead(8) == digitalRead(9)) {
    encoderPositionD++;
  }
  else {
    encoderPositionD--;
  }
}
