/* Code that will turn on the Jetson TX2/1
   whenever power is available
*/

#define switchPin 14 // Active low signal to turn on Jetson
#define pwrInPin 15 // Hooked up to the power LED on the Jetson
#define LEDPin 13 // Onboard LED on teensy

void setup() {
  // put your setup code here, to run once:
  pinMode(switchPin, OUTPUT); // power switch pin
  pinMode(LEDPin, OUTPUT); // LED on teensy/arduino board
  pinMode(pwrInPin, INPUT); // power detection pin

  digitalWrite(switchPin, HIGH); // This pin is active low
  digitalWrite(LEDPin, LOW); // turn the LED off
  delay(1000); // small delay from power on until we turn on the jetson
}

void pressSwitch() {
  digitalWrite(switchPin, LOW);
  digitalWrite(LEDPin, HIGH);
  delay(500);
  digitalWrite(switchPin, HIGH);
  digitalWrite(LEDPin, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (!digitalRead(pwrInPin)) {
    pressSwitch();
  }
  delay(5000);
}
