#ifndef __JSON_HPP__
#define __JSON_HPP__
#include <ArduinoJson.h>

namespace json {
    struct Data {
        static const int NUM_ENCODERS = 4;
        static const int NUM_SENSORS = 7;
        static Data data;
        double sensors[NUM_ENCODERS];
        double encoderSpeeds[NUM_SENSORS];
        unsigned int hallEffect;
        void sendJson();
    private:
        Data();
    };
}
#endif