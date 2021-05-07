#include "HallEffect.hpp"
#include "Json.hpp"
void hallEffect::readHallEffect() {
    json::Data::data.hallEffect = (rand() % 1000);
}

void hallEffect::initHallEffect() {
    // pinMode(13, INPUT_PULLUP);
}