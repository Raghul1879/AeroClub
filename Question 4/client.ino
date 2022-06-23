/*
Name: Raghul S
Roll No: EE20B103

This is a client code. The message received by the client from server will be 
printed on the Serial monitor and if the message says "measure temp" then our
ESP32 will start measuring the temperature using an analog temperature sensor
and if the temperature is above 45 centigrade, the buzzer will start making noise
as a sign of alert. 

*/

#include <WiFi.h>

const char* ssid="Wokwi-GUEST";  //Enter you network name 
const char* password="";       //Enter your wifi password

const int port = 9090;      //Enter a port number of server
const char* host = "192.168.29.126";    //Enter ipv4 of the server
                                     // connected to your local network
int incomingByte = 0; 
char name[100];
int i=0;
char name1[100]="measure temp";

int buzzerPin = 13;
int BETA = 3950;
float celsius = 0;

void setup() 
{
  Serial.begin(115200);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.println("...");
  }
  Serial.println("Wi-Fi connected with IP: ");
  Serial.println(WiFi.localIP());
  pinMode(34, INPUT);
  pinMode(13, OUTPUT);
}

void loop() 
{
  WiFiClient client;
  if(!client.connect(host, port)){
    Serial.println("Not connected");
    delay(3000);
    return;
  }

  Serial.println("Connected to server successfully");

  if (client.available() > 0) {
    // read the incoming byte:
  incomingByte = client.read();

    // say what you got:
  name[i]=(char)incomingByte;     
Serial.print((char)incomingByte);   //To print the message on Serial monitor
  i++;
  }

  if(strcmp(name,name1)==0){
  for(int j=0;;j++){
  int analogValue = analogRead(34);
  celsius = 1 / (log(1 / (4095. / analogValue - 1)) / BETA + 1.0 / 298.15) - 273.15;
  if(celsius<45){
    digitalWrite(13,HIGH);
    delayMicroseconds(100);
    digitalWrite(13,LOW);
    delayMicroseconds(100);
  }
  }

}
  
}