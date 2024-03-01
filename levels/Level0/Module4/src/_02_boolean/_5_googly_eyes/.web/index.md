
 <div id="recipeLeftColumn">
  # Googly Eyes
  <hr/>
  <img alt="Googly image" src="./googlyEyes.png"/>
  <div id="recipeGoal">
   ## Goal:
   You’re going to draw a face with eyes that will follow the mouse!
  </div>
 </div>
 <div id="recipeRightColumn">
  <div id="recipeSteps">
   ## Steps:
   <ol>
    <li>
     Find the Googly Eyes recipe program in Eclipse.
    </li>
    <li>
     Find an image on the internet and copy it to the
     <b>
      /images
     </b>
     folder. It can be anything as long as it has large eyes!
    </li>
    <li>
     On line 1 of your program (outside of the methods) declare a variable for the image:
     ```
   PImage face;

```
    </li>
    <li>
     In your setup() method, import your image using the following code:
     ```

    face = loadImage(“face.jpg”);

```
    </li>
    <li>
     If you need to, change the code you just entered so that "face.jpg" matches the name of your picture.
    </li>
    <li>
     Set the size of your window and the size of your image to be the same by entering the following code in the setup method.
     ```
    size(800,600);
    face.resize(width,height);

```
    </li>
    <li>
     In the draw() method, place a white ellipse over the left eye of your image.
     HINT: To find out where to put it, add code to print the mouseX and mouseY where you click the mouse.
    </li>
    <li>
     Now add a pupil (the black part) to the left eye earlier.
    </li>
    <li>
     Use mouseX and mouseY to move the left pupil where the mouse moves.
    </li>
    <li>
     Add a white ellipse over the right eye using the same technique used for the left eye.
    </li>
    <li>
     Add a right pupil and make it move by using mouseX + [distance from left eye] and mouseY + [distance from left eye].
    </li>
    <li>
     Here’s the tricky part: stop the pupils from going outside of the white circles!  To do this, imagine a rectangle that the pupil should stay within.  When mouseX and mouseY goes outside of these bounds, set it back to the boundary.  Put this code before you draw the pupils.
    </li>
    <li>
     Make sure you SAVE YOUR CODE when you are done.
    </li>
   </ol>
  </div>
 </div>

