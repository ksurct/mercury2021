#include "Sensors.hpp"
#include "Json.hpp"
void sensors::readSensors() {
    for (int i = 0; i < json::Data::NUM_SENSORS; i++) {
        json::Data::data.sensors[i] = (double)(rand() % 100) / 100.0;
    }
}

void sensors::initSensors() {

}