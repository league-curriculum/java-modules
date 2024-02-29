<body><div id="wrap"><div id="main">
<div id="recipeLeftColumn"># Pong
<hr/>
<img src="images/pong.png"/>
<div id="recipeGoal">## Goal:
Make a Pong game using Processing!</div>
</div>
<div id="recipeRightColumn"><div id="recipeSteps">## Steps:
<ol id="stepList">
<li>Draw a ball on the screen.
```

ellipse(x, y, width, height) //in draw method
fill(red, green, blue) //in draw method
stroke(red, green, blue) //in draw method

```
</li><li>Make the ball move across the screen (left to right).
...make a variable for the ball's X position and change it in the draw method.

</li><li>Change the speed of the ball.
<ol class="insetRecipeStepsOL">
<li>make a variable for the speed of the ball in the X direction (from left to right).</li>
<li>changing this variable should change the speed of your ball</li>
</ol>
</li><li>Make the ball bounce off of the walls.
```

if(x &gt; width){
    xSpeed = -xSpeed;
}

```
</li><li>Do the same in the Y (up and down) direction.
(hint) height

</li><li>Add a background image for your game.
```

PImage backgroundImage; //at the top of your sketch
backgroundImage = loadImage("image.jpg"); //in the setup method
image(backgroundImage, 0, 0); //in draw method
image(backgroundImage, 0, 0, width, height); //if you want to resize

```
</li><li>Draw a paddle at the bottom of the screen
```

rect(x, y, width, height);

```
</li><li>Use mouseX to make the paddle move over and back with the mouse.

</li><li>Make the ball change Y direction when it hits the paddle. Figure it out by yourself, or use this
method:
```

boolean intersects(int ballX, int ballY, int paddleX, int paddleY,
int paddleLength) {
    if (ballY &gt; paddleY &amp;&amp; ballX &gt; paddleX &amp;&amp; ballX &lt; paddleX + paddleLength)
        return true;
    else
        return false;
}

```
</li> <li>Make sure you SAVE YOUR CODE when you are done. 
            </li>
</ol>
<div id="p3link"></div>
<div style="clear:both;"></div></div></div></div></div><div id="footer"></div></body>