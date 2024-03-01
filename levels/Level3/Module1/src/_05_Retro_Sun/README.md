
# Retro Sun (Processing)
### Part 1: Drawing the Sun
  
   <img alt="" src="./1_sun.png" style="width: 400px; height: 330px;"/>
   Open the starter code in Processing.
Draw and fill a solid color ellipse to be the sun.
### Part 2: Drawing a color gradient on the sun
   
    <img alt="" src="./2_gradient.png" style="width: 400px; height: 180px;"/>
    Change the sun-colored pixels in your sketch make the sun have gradually different colors from the top to bottom.

Use the interpolateColor() method to find which color to change the pixel.
```

// Input variable 'step' is a value from 0.0 to 1.0, where
// 0.0 is the top of the sun and 1.0 is the bottom
interpolateColor(color[] arr, float step)
```
### Part 3: Drawing the missing sections at the bottom of the sun
    
     <img alt="" src="./3_missing_sun_section.png" style="width: 400px; height: 180px;"/>
     The missing parts of the sun are created by drawing rectangles over the sun with the same color as the background.
### Part 4: Moving the missing sun sections
     
      <img alt="" src="./4b_resizing_section.gif" style="width: 400px; height: 330px;"/>
      To move a section upwards each rectangle's y value needs to decrease.
To make the section get smaller, its height value needs to also decrease.
### Part 5: Managing the missing sun sections
      
       <img alt="" src="./5_multiple_sections.gif" style="width: 400px; height: 225px;"/>
       Using a List to manage moving multiple missing sun sections
### Part 6: Adding reflections, stars, and other extras
       
        <img alt="" src="./6_retro_sun_extras.gif" style="width: 400px; height: 225px;"/>
        If you want to make your retro sun look more unique, try adding reflections and stars. You may use the example classes below.
```

class Star {
  int x;
  int y;
  color starColor;
  float startAlpha;
  float alpha;
  float diameter;

  Star(int x, int y, color col) {
    this.x = x;
    this.y = y;
    starColor = col;
    this.diameter = random(0.1, 3);
    this.startAlpha = random(1, 200);
    this.alpha = startAlpha;
  }
  
  void setAlpha(int alpha){
    this.alpha = constrain(alpha, startAlpha, 255);
  }

  void draw() {
    noStroke();
    fill(starColor, alpha);
    float blink = random(0, 0.8);
    ellipse(x, y, diameter + blink, diameter + blink);
  }
```
```

class Reflection {
/*
  // HSB colors
  color[] barColors = {
    color(285, 96.6, 23.1), 
    color(312, 100, 42.7), 
    color(340, 66.9, 60.4), 
    color(11, 60.8, 62), 
    color(340, 66.9, 60.4), 
    color(312, 100, 42.7), 
    color(285, 96.6, 23.1)
  };
*/
  // RGB colors
  color[] barColors = {
    color(45, 2, 59), 
    color(109, 0, 88), 
    color(154, 51, 86), 
    color(158, 79, 62), 
    color(154, 51, 86), 
    color(109, 0, 88), 
    color(45, 2, 59)
  };

  int sunRadius;
  int numReflectionBars;
  int topX;
  int topY;
  int topWidth;
  int bottomY;
  int maxHeight;
  float speed;
  ArrayList lowerBars;
  
  Reflection(int sunRadius, int numBars, int topX, int topY, float speed){
    this.sunRadius = sunRadius;
    this.topX = topX;
    this.topY = topY;
    this.speed = speed;

    initialize(numBars);
  }
  
  void initialize(int numBars){
    this.numReflectionBars = numBars;
    
    topWidth = 2 * (sunRadius + sunRadius/3);
    maxHeight = 10;
    bottomY = topY + (numBars * 2 * maxHeight);
    lowerBars = new ArrayList();
    
    // Setup bottom relection bars
    int x = topX;
    int y = topY;
    int w = topWidth;
    int h = maxHeight;
    for ( int i = 0; i < numReflectionBars; i++ ) {   
      y += (bottomY - topY) / numBars;
      x += sunRadius / 16;
      w -= 2 * (sunRadius / 16);

      Rectangle r = new Rectangle(x, y, w, h);
      lowerBars.add(r);
    }
  }
  
  void draw(){
    strokeWeight(1);
    
    for ( Rectangle bar : lowerBars ) {
      for ( int i = (int)bar.x; i < bar.x + bar.w; i++ ) {
        float alphaMax = -255 - (bar.y - topY);
        float alphaMin =  255 + (bar.y - topY);
        float alpha = map(i, bar.x, bar.x + bar.w, alphaMin, alphaMax);
        float step = map(i, bar.x, bar.x + bar.w, 0, 1);
        color lc = interpolateColor(barColors, step);
    
        stroke(lc, 255 - abs(alpha));
        line(i, bar.y, i, bar.y + bar.h);
      }
      
      bar.y += speed;
      bar.x += speed;
      bar.w -= 2 * speed;

      if( bar.y > bottomY ) {
        // Bar at bottom, reset to top
        
        bar.x = topX;
        bar.y = topY + maxHeight;
        bar.w = topWidth;
        bar.h = 1;
      } else if( bar.y > bottomY - maxHeight ) {
        // Bar near bottom
        
        bar.h -= speed;
      } else if( bar.h < maxHeight ) {
        // Bar height just reset and at top
        
        bar.y -= speed;
        bar.h += speed;
      }
    }
  }
}
```
       
      
     
    
   
  
 

