#include <Servo.h>

Servo myServo;

int trigPin = D5;
int echoPin = D6;

long duration;
int distance;

void setup()
{
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);

    Serial.begin(9600);

    myServo.attach(13, 500, 2400);
}

void loop()
{
    for (int angle = 0; angle <= 180; angle += 2)
    {
        scan(angle);
    }

    for (int angle = 180; angle >= 0; angle -= 2)
    {
        scan(angle);
    }
}

void scan(int angle)
{
    myServo.write(angle);
    delay(60);  

    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);

    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH, 20000);
    distance = duration * 0.034 / 2;

    if (distance == 0 || distance > 200) return;

    Serial.print(angle);
    Serial.print(",");
    Serial.println(distance);
}