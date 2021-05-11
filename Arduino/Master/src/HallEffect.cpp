#include "HallEffect.hpp"
#include "Json.hpp"
void hallEffect::readHallEffect() {
    json::Data::data.hallEffect = analogRead(A0);
}

void hallEffect::initHallEffect() {
}