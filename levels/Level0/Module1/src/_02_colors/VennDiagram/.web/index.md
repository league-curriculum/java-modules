<body>
<div id="wrap">
<div id="main">
<div id="recipeLeftColumn">
# Venn Diagram of Me

<hr/>
<img alt="Venn Diagram of me image" src="images/vennDiagram.png"/>
<div id="recipeGoal">
## Goal:


Use the RGB color model to create a Venn Diagram that showcases your personality.

</div>
</div>
<div id="recipeRightColumn">
<div id="recipeSteps">
## Steps:

<ol id="stepList">
<li>Find the Venn Diagram recipe program ( VennDiagram.pde ) and open it using Processing.</li>
<li>Run the program and you should see an empty gray window.</li>
<li>After the size() command, add code to draw 3 circles to form a Venn Diagram (see picture).
                            The command to draw a circle in Processing is:

```
ellipse (centerX, centerY, circleWidth, circleHeight);
```
<li>Change the x and y of each ellipse until they overlap as in the picture. 
                        </li>
<li>Run the program. It should look a bit like this<img src="images/whiteCircles.png"/></li>
<li>Now to add the colors. Processing uses the following command to draw in color:

```
fill(red, green, blue, opacity);
```

where red, green, blue, and opacity are all numbers between 0 and 255. So to make see-through red circles, we add the following line of code BEFORE we draw the circles.

```
fill(255, 0, 0, 100);
```

<li>Run the program. It should look a bit like this<img src="images/redCircles.png"/> We can now see the edges of all the circles because we made them "see-through" by setting the opacity to 100 (which is &lt; 255)</li>
<li>Add more fill commands (you will have to figure out where to put them) so that each ellipse has its own unique color.<img src="images/colorfulCircles.png"/></li>
<li>Label each of the circles with an aspect of your personality. Processing uses the following command to draw text. You will need to put numbers in place of xLocation, and yLocation. Play around with the x and y until it works with your diagram.

```
text("TEXT", xLocation, yLocation);
```
</li>
<li>You can also make the text larger by changing the sizeOfLetters (you will have to figure out where to put this)
```
textSize(sizeOfLetters);
```
</li>
</li></li></ol>
<div id="p3link"></div>
<div style="clear:both;"></div>
</div>
</div>
</div>
</div>
<div id="footer">

</div>
</body>