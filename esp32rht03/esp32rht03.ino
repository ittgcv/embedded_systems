/***************************************************** 
* Captura temperatura ambiente, humedad exterior y humedad del suelo
* DHT Input: ==> GPIO23.
* Transmite datos almacenados via bluetooth
* MJRoBot.org 9Sept17
*****************************************************/

/* DHT */
#include "DHT.h"
#include "BluetoothSerial.h"
#define DHTPIN 23  
#define DHTTYPE DHT22 
#define MOISTURE_SENSOR 36

DHT dht(DHTPIN, DHTTYPE);
BluetoothSerial SerialBT;
float localHum = 0;
float localTemp = 0;
int valHumedadSuelo=0;
int contadorlocal=0;
int contadorexterno=0;
int lecturasTemperatura[500];
int lecturasHumedadAmbiente[500];
int lecturasHumedadSuelo[500];
/*WiFi.mode(WIFI_OFF);
      btStop();      btStart();
 WiFi.begin(STA_SSID, STA_PASS);*/
void setup()
{
  Serial.begin(115200);
  delay(1000); // give me time to bring up serial monitor
  Serial.println("");
  Serial.println("ESP32 DHT Temperature and Humidity ");
  Serial.println("");
  dht.begin();
  SerialBT.begin("ESP32");
}

void loop()
{
  getDHT();
  Serial.print("Temp: ==> ");
  Serial.print(localTemp);
  Serial.print("  Hum ==> ");
  Serial.println(localHum);
  lecturasTemperatura[contadorlocal]=localTemp;
  lecturasHumedadAmbiente[contadorlocal]=localHum;
  getMoisture();
  lecturasHumedadSuelo[contadorlocal]=valHumedadSuelo;
  Serial.print("Humedad suelo==> ");
  Serial.println(valHumedadSuelo);
  contadorlocal=contadorlocal+1;
  Serial.print("  contadorlocal ==> ");
  Serial.println(contadorlocal);
  if (SerialBT.available()>0)
  {
    sendDataBT();
  }
  delay(1800000);
}
void sendDataBT()
{
  Serial.println(SerialBT.read());  // vacia el buffer
  while (contadorlocal>0)
  {
    SerialBT.println(lecturasTemperatura[contadorlocal]);
    SerialBT.println(lecturasHumedadAmbiente[contadorlocal]);
    SerialBT.println(lecturasHumedadSuelo[contadorlocal]);
    contadorlocal=contadorlocal-1;
  }
}
/***************************************************
* Get indoor Temp/Hum data
****************************************************/
void getDHT()
{
  localTemp = map(dht.readTemperature(),0,1023,20,30);
  localHum = map(dht.readHumidity(),0,1023,20,30);
  return;
}
void getMoisture() {
  int analogValue=analogRead(MOISTURE_SENSOR);
  valHumedadSuelo=analogValue;
  return;
}
