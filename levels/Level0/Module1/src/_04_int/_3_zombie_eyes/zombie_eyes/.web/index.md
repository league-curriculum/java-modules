
 <div id="recipeLeftColumn">
  # Zombie Eyes
  <hr/>
  <img alt="Zombie Eyes image" src="http://level0.jointheleague.org/modules/Mod1Recipes/images/zombieEyes.png       "/>
  <div id="recipeGoal">
   ## Goal:
   You are going to make a face with animated eyes. You could use your own face (if you have a photo) or a zombie, a cat, or whatever you like. Whatever you choose, the eyes should be prominent (large).
  </div>
 </div>
 <div id="recipeRightColumn">
  <div id="recipeSteps">
   ## Steps:
   <ol id="stepList">
    <li>
     Find the Zombie Eyes recipe program ( zombie_eyes.pde ) and open it using Processing.
    </li>
    <li>
     Drop the image of a face onto your sketch. Load it like this in the setup method:
     ```

PImage face = loadImage("face.jpeg");

```
    </li>
    <li>
     Adjust the size of your sketch if necessary.
     ```

size(width, height);

```
    </li>
    <li>
     Adjust the size of your image so that the size matches the sketch and draw it using the image command.
     ```

face.resize(width, height);
image(face, 0, 0);

```
    </li>
    <li>
     Place 2 ellipses over the irises of the eyes in the draw method.
     ```

ellipse(x, y, width, height);

```
    </li>
    <li>
     Give the irises a color with the fill command (use numbers in place of red, green, blue).
     ```

fill(red, green, blue);

```
    </li>
    <li>
     Use mouseX and mouseY to change the color of the irises when the mouse moves.
    </li>
    <li>
     Draw black pupils on top of the irises.
    </li>
    <li>
     Make sure you SAVE YOUR CODE when you are done.
    </li>
   </ol>
  </div>
 </div>

