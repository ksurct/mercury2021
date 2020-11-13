class 
int maxLengthInput = 30;

void startUp() {
	Serial.begin(9600, SERIAL_8O1)
}

void send8Bits(char x) {
	
	Serial.write(x);
}

/**
 * Reads bytes until hits max length or it hits the \0 char
 * 
 **/
char* getInputMessage() {
	char* x[maxLengthInput];
	if (!Serial.available()) {
		return 0;
	}
	return Serial.readBytesUntil('\0', x);
}

void setMaxLengthInput(int x) {
  maxLengthInput = x;
}
