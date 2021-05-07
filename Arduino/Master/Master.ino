#include "Arduino.h"
#include "src/Encoders.hpp"
#include "src/HallEffect.hpp"
#include "src/Json.hpp"
#include "src/Sensors.hpp"


void setup() {
    Serial.begin(115200);
    sensors::initSensors();
    encoders::initInterrupts();
    hallEffect::initHallEffect();
}

const uint32_t UPDATE_INTERVAL = 750;
unsigned long long timer = millis();
void loop() {
    if (millis() - timer >= UPDATE_INTERVAL) {
        Serial.print("\nInterval:\n");
        // read and aggregate sensor data.
        sensors::readSensors();

        // get hall effect data
        hallEffect::readHallEffect();

        // Get encoder speeds
        encoders::getEncoderSpeeds();

        json::Data::data.sendJson();
        timer += UPDATE_INTERVAL;
        delay(750);
    }
    // // check pin 13 for high 
    // if (digitalRead(13) == HIGH) {
    //     json::Data::data.sendJson();
    // }
}