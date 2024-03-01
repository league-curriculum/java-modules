
 # Level 0 Study Guide
 ### 
Variables
 ‘Declare and initialize a variable’ means make a variable and give it a value.
 int age = 12; 
String name = “Sarah”;
 Remember, String is capitalized and the value always has quotes around it.
 Every time you want to hold a new piece of information you need to declare the variable and initialize it, by setting it equal to something.
 If you want to generate a random number you do it like this.
 int x = new Random().nextInt(10);
 The number in parenthesis limits the value of the random number you will get. In this case, x will be a number between 0 and 9.
 ### 
if Statements
 if (condition){

}
else if (next condition){

}
else{

}
 The question looks like this for a String
 (name .equals (“Sarah”))
 You use .equals to compare a String. The String value is in parenthesis and in quotes.
 The question looks like this for an int
 (age == 12)
 Remember you use == for a comparison.
 It is a good idea to use an else with an if statement to catch any options you didn’t think of.
 ### 
for loop
 for ( int i = 0; i&lt;10; i++){

}
 <font color="green">
  int i = 0;
 </font>
 This is the starting point of the loop. You must declare the int.
 <font color="green">
  i&lt;10;
 </font>
 This is the finishing point for the loop. The loop will continue as long as i is less than 10.
 i++ This is how much the loop counter changes by each time. In this case it increments (goes up) by 1.
 for ( int i = 10; i&gt;0; i-=2){

}
 This loop counts down in 2s starting at 10.
10, 8 , 6, 4, 2.  It doesn’t go to 0 because it must be greater than 0.
Notice that you have to change from less than (&lt;) to greater than (&gt;) when you count down.
 ### 
JOptionPane
 If you want a pop up to give the user a message use
 JOptionPane.showMessageDialog(null, “Hello ”+ name);
 Don’t forget the
 <b>
  null
 </b>
 , or that any text needs to be in quotes.
 If you want to get an answer from the user, use:
 String ageString = JOptionPane.showInputDialog(“How old are you?”);
 Remember you must catch the user’s answer in a String, otherwise you can’t use it.
 Because the answer is always a String, you sometimes want to convert it to a number so you can do a calculation. This is how you do it.
 int age = Integer.parseInt(ageString);
 If you want to write something to the console, instead of using a pop-up
 System.out.println(age);
 ### Methods
 You must have a
 <b>
  main method
 </b>
 in order to start your class running.
 public static void main(String[] args){

}
 Other methods looks like this
 void drawSquare(){
 for (int i= 0; i&lt;4; i++){
  Tortoise.move(100);
  Tortoise.turn(90);
 }
}
 <font color="green">
  void
 </font>
 This tells you what the method will return - in this case nothing.
 <font color="green">
  drawSquare
 </font>
 This is the name of the method, that you use to call it.
 <font color="green">
  (  )
 </font>
 This tells you what parameters the method needs. In this case it doesn’t need any.
 You call the method like this:
 drawSquare();
 Look at this method:
 int sevenTimes(int number){
	 return number * 7;
}
 <font color="green">
  int
 </font>
 This method is going to a return an int so you need to create an int variable to store it. In the example below, the variable is named "answer".
 <font color="green">
  sevenTimes
 </font>
 This is the name of the method, that you use when you call it.
 <font color="green">
  (int number)
 </font>
 This tells you what parameters the method needs. In this case it needs you to give an int. In the example below, the int is the number 2.
 int answer = sevenTimes(2);
 The value of answer will be 14.
 ### 
Modulo

Modulo means remainder.
The value of 11%5 is 1, because 5 goes into 11, 2 times (5x2=10) with a remainder of 1.

It is useful to use modulo to alternate between options. e.g.
 
for (int i = 0; i&lt;1000;i+=10){
 	if (i%3==0){
  		fill(255,0,0);
 	}
 	else if (i%3==1){
  		fill(0,255,0);
 	}
 else if (i%3==2){
	  	fill(0,0,255);
	 }
	 ellipse(i,i,10,10);
}

This code will draw a line of circles alternating in red, green and blue.

