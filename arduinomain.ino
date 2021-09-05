#include <LM35.h>

LM35 temp(A0);
String cad, cad1, cad2, cad3, cad4;
int pos, pos2, pos3, pos4;
float temperatura;
int LED = 13;
int R = 9;
int G = 10;
int B = 11;

void Decod(String cadena){
    pos = cadena.indexOf(',');
    cad1 = cadena.substring(0,pos);
    pos2 = cadena.indexOf(',',pos+1);
    cad2 = cadena.substring(pos+1,pos2);
    pos3 = cadena.indexOf(',',pos2+1);
    cad3 = cadena.substring(pos2+1,pos3);
    pos4 = cadena.indexOf(',',pos3+1);
    cad4 = cadena.substring(pos3+1,pos4);
}

void setup() {
pinMode(A0, INPUT);
pinMode(LED, OUTPUT);
pinMode(R, OUTPUT);
pinMode(G, OUTPUT);
pinMode(B, OUTPUT);
Serial.begin(9600);
Serial.setTimeout(50);
}


void loop() {
  temperatura = temp.cel();
  if (Serial.available())
  {
    cad = Serial.readString();
    switch(cad.toInt()){
      case 1001:
        digitalWrite(LED, HIGH);
        break;
      case 1010:
        digitalWrite(LED, LOW);
        break;
      case 1011:
        Serial.println(temperatura);
        Serial.print("");
        break;
    }
    Decod(cad);
    if (cad1.toInt() == 2)
    {
      analogWrite(R, cad2.toInt());
      analogWrite(G, cad3.toInt());
      analogWrite(B, cad4.toInt());
    }
  }
} 
