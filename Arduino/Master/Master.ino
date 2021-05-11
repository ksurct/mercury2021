#include "Arduino.h"
#include "src/Encoders.hpp"
#include "src/HallEffect.hpp"
#include "src/Json.hpp"
#include "src/Sensors.hpp"
#define SIGNAL_PIN 2
#define DBG_SEND_JSON_ON_INTERVAL true
void signalISR() {
    Serial.println("Test");
    json::Data::data.sendJson();
}

void setup() {
    Serial.begin(115200);
    pinMode(SIGNAL_PIN, INPUT_PULLDOWN);
    attachInterrupt(digitalPinToInterrupt(SIGNAL_PIN), signalISR, RISING);
    sensors::initSensors();
    encoders::initInterrupts();
    hallEffect::initHallEffect();
}

const unsigned long long UPDATE_INTERVAL = 500;
unsigned long long timer = millis();
void loop() {
    if (millis() - timer >= UPDATE_INTERVAL) {
        // read and aggregate sensor data.
        sensors::readSensors();

        // get hall effect data
        hallEffect::readHallEffect();

        // Get encoder speeds
        encoders::getEncoderSpeeds();
        if (DBG_SEND_JSON_ON_INTERVAL) {
            json::Data::data.sendJson();
        }
        timer = millis();
    }
}