

const int Input_1 = 1;
const int Input_2 = 2;
const int Input_3 = 3;
const int Input_4 = 4;

const int Enable_Left = 5;
const int High_Left = 6;       
const int Low_Left = 7;

const int Enable_Right = 10;
const int High_Right = 8;       
const int Low_Right = 9;

int Input1;
int Input2;
int Input3;
int Input4;



void setup() {

pinMode(Input_1, INPUT);
pinMode(Input_2, INPUT);
pinMode(Input_3, INPUT);
pinMode(Input_4, INPUT);

pinMode(Enable_Left, OUTPUT);
pinMode(High_Left, OUTPUT);
pinMode(Low_Left, OUTPUT);


pinMode(Enable_Right, OUTPUT);
pinMode(High_Right, OUTPUT);
pinMode(Low_Right, OUTPUT);



}


void Forward()
{
  digitalWrite(High_Left, HIGH);
  digitalWrite(Low_Left, LOW);
  analogWrite(Enable_Left,90);

  digitalWrite(High_Right, LOW);
  digitalWrite(Low_Right, HIGH);
  analogWrite(Enable_Right,80);
  
}


void Backward()
{
  digitalWrite(High_Left, LOW);
  digitalWrite(Low_Left, HIGH);
  analogWrite(Enable_Left,100);

  digitalWrite(High_Right, HIGH);
  digitalWrite(Low_Right, LOW);
  analogWrite(Enable_Right,90);
  
}

void Left_1()
{
  digitalWrite(High_Left, HIGH);
  digitalWrite(Low_Left, LOW);
  analogWrite(Enable_Left,60);

  digitalWrite(High_Right, LOW);
  digitalWrite(Low_Right, HIGH);
  analogWrite(Enable_Right,100);
  
}

void Left_2()
{
  digitalWrite(High_Left, HIGH);
  digitalWrite(Low_Left, LOW);
  analogWrite(Enable_Left,0);

 digitalWrite(High_Right, LOW);
  digitalWrite(Low_Right, HIGH);
  analogWrite(Enable_Right,100);
  
}

void Left_3()
{
  digitalWrite(High_Left, LOW);
  digitalWrite(Low_Left, HIGH);
  analogWrite(Enable_Left,100);

  digitalWrite(High_Right, LOW);
  digitalWrite(Low_Right, HIGH);
  analogWrite(Enable_Right,100);
  
}

void Right_1()
{
  digitalWrite(High_Left, HIGH);
  digitalWrite(Low_Left, LOW);
  analogWrite(Enable_Left,100);

  digitalWrite(High_Right, LOW);
  digitalWrite(Low_Right, HIGH);
  analogWrite(Enable_Right,60);
  
}

void Right_2()
{
  digitalWrite(High_Left, HIGH);
  digitalWrite(Low_Left, LOW);
  analogWrite(Enable_Left,100);

  digitalWrite(High_Right, LOW);
  digitalWrite(Low_Right, HIGH);
  analogWrite(Enable_Right,0);
  
}

void Right_3()
{
  digitalWrite(High_Left, HIGH);
  digitalWrite(Low_Left, LOW);
  analogWrite(Enable_Left,100);

  digitalWrite(High_Right, HIGH);
  digitalWrite(Low_Right, LOW);
  analogWrite(Enable_Right,100);
  
}

void Stop()
{

  analogWrite(Enable_Left, 0);
  analogWrite(Enable_Right, 0);
}

void loop() 
{

   Input1 = digitalRead(Input_1);
   Input2 = digitalRead(Input_2);
   Input3 = digitalRead(Input_3);
   Input4 = digitalRead(Input_4);
  
  if (Input1 == HIGH && Input2 == LOW && Input3 == LOW && Input4 == LOW)
    Forward();

  if (Input1 == LOW && Input2 == HIGH && Input3 == LOW && Input4 == LOW)
    Backward();

   if (Input1 == LOW && Input2 == LOW && Input3 == HIGH && Input4 == LOW) 
    Left_3();

   if (Input1 == LOW && Input2 == LOW && Input3 == LOW && Input4 == HIGH)
    Right_3();

   if (Input1 == HIGH && Input2 == HIGH && Input3 == LOW && Input4 == LOW)
    Stop();

}
