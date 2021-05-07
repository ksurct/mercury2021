#include "Encoders.hpp"
#include "Json.hpp"
using namespace json;
void encoders::getEncoderSpeeds() {
    for (int i = 0; i < Data::NUM_ENCODERS; i++) {
        Data::data.encoderSpeeds[i] = (double)(rand() % 100) / 100.0;
    }
}

void encoders::initInterrupts() {

}
