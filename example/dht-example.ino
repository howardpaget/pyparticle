// Based on the DHT and BMP085 examples written by ladyada

#include "Adafruit_BMP085/Adafruit_BMP085.h"
#include "Adafruit_DHT/Adafruit_DHT.h"

#define DHTPIN 2

//#define DHTTYPE DHT11		// DHT 11
#define DHTTYPE DHT22		// DHT 22 (AM2302)
//#define DHTTYPE DHT21		// DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

int power = D5;

DHT dht(DHTPIN, DHTTYPE);
Adafruit_BMP085 bmp;

double humidity = -1;
double temperature_dht = -274;
double temperature_bmp = -274;
double pressure = -1;

void setup(){
    Particle.publish("message", "Mini Weather Station Starting");

    Particle.function("set_led", setLED);

    Particle.variable("humidity", humidity);
    Particle.variable("temp_dht", temperature_dht);
    Particle.variable("temp_bmp", temperature_bmp);
    Particle.variable("pressure", pressure);

    pinMode(D6, OUTPUT);

    pinMode(power, OUTPUT);
    digitalWrite(power, HIGH);

    dht.begin();
    bmp.begin();
}

void loop(){
    delay(2000);

    float h = dht.getHumidity();
    float t_dht = dht.getTempCelcius();
    float t_bmp = bmp.readTemperature();
    float p = bmp.readPressure() / 100.0;

    if(!isnan(h) && h > 0)
        humidity = h;

    if(!isnan(t_dht) && t_dht > -274)
        temperature_dht = t_dht;

    if(!isnan(t_bmp) && t_bmp > -274)
        temperature_bmp = t_bmp;

    if(!isnan(p) && p > 0)
        pressure = p;
}

int setLED(String command){
    if(command == "on"){
        digitalWrite(D6, HIGH);
        return 1;
    }else if(command == "off"){
        digitalWrite(D6, LOW);
        return 0;
    }
    return -1;
}
