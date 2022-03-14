#include "DHT.h"

#define DHTPIN 2     // what digital pin we're connected to
#include <Servo.h>

Servo myservo;  // create servo object to control a servo

// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 22  (AM2302), AM2321
DHT dht(DHTPIN, DHTTYPE);
const int ledPin =  LED_BUILTIN;// the number of the LED pin
const int relayPin =  9;// the number of the LED pin
unsigned long previousMillis = 0;        // will store last time LED was updated
// Variables will change:
int ledState = LOW;             // ledState used to set the LED

// constants won't change:
const float interval = 3600000;           // interval at which to blink (milliseconds)

void setup() {
  Serial.begin(115200);
  dht.begin();
  pinMode(ledPin, OUTPUT);
  pinMode(relayPin, OUTPUT);
  myservo.attach(8);  // attaches the servo on pin 9 to the servo object
}
 
void loop() {
  Serial.println("Sniper Technology");
  unsigned long currentMillis = millis();
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print("Humidity: ");
  Serial.print(100-h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" *C ");
  Serial.print(f);
  Serial.print(" *F\t");
  Serial.print("Heat index: ");
  Serial.print(hic);
  Serial.print(" *C ");
  Serial.print(hif);
  Serial.println(" *F");
  if (t<37.2) {
    //digitalWrite(ledPin, HIGH);
    digitalWrite(relayPin, HIGH);
    Serial.println("Calentando");
  }
  if (t>38.0) {
    //digitalWrite(ledPin, LOW);
    digitalWrite(relayPin, LOW);
    Serial.println("Enfriando");
  }
  if (currentMillis - previousMillis >= interval) {
    // save the last time you blinked the LED
    previousMillis = currentMillis;

    // if the LED is off turn it on and vice-versa:
    if (ledState == LOW) {
      ledState = HIGH;
      myservo.write(30);                  // sets the servo position according to the scaled value
    } else {
      ledState = LOW;
      myservo.write(150);                  // sets the servo position according to the scaled value
    }

    // set the LED with the ledState of the variable:
    digitalWrite(ledPin, ledState);
  }
  Serial.println((currentMillis - previousMillis)/60/60);


  delay(1000);  // delay de un segundo
}
