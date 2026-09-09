#define TRIGGER 3
#define ECHO 5
#define BUZZER 7


unsigned long timer = 0;

void setup() {
  Serial.begin(9600);
  pinMode(TRIGGER, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(BUZZER, OUTPUT);    
}

void loop() {
  if (millis() - timer > 30){
    digitalWrite(TRIGGER, LOW);
    delayMicroseconds(2);

    digitalWrite(TRIGGER, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER, LOW);

    long duracao = pulseIn(ECHO, HIGH, 25000);
    int distancia = duracao * (0.034 / 2);

    Serial.print("Distancia:"); Serial.println(distancia);

    if (distancia > 0 && distancia < 40) {
      digitalWrite(BUZZER, HIGH);
    }else {
      digitalWrite(BUZZER, LOW);
    }

    timer = millis();
  }

}
