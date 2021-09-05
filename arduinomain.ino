#include <LM35.h>

LM35 temp(A0);
String cad;
float temperatura;
int LED = 13;


void setup() {
pinMode(A0, INPUT);
pinMode(LED, OUTPUT);
Serial.begin(9600);
Serial.setTimeout(50);
}


void loop() {
  temperatura = temp.cel();
  if (Serial.available())
  {
    cad = Serial.readString();
    if (cad.toInt() == 1001)
    {
      digitalWrite(LED, HIGH);
    }
    else if (cad.toInt() == 1010)
    {
      digitalWrite(LED, LOW);
    }
    else if (cad.toInt() == 1011)
    {
      Serial.println(temperatura);
      Serial.print("");
    }
  }
} 
