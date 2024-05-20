package _02_colors.VennDiagram;

import processing.core.PApplet;

public class VennDiagramOfMe extends PApplet {

        @Override
    public void draw() {
        background(255); // Ensuring background is white to see the drawings

        fill(0, 250, 0, 100);
        ellipse(350, 250, 200, 200);
        
        fill(250, 0, 0, 100);
        ellipse(200, 250, 200, 200);

        fill(0, 0, 250, 100);
        ellipse(275, 350, 200, 200);

        fill(0, 0, 0, 100);
        textSize(25);
        text("angry", 150, 200);
        text("happy", 325, 200);
        text("sad", 250, 375);
    }


    public static void main(String[] args) {
        VennDiagramOfMe vdom = new VennDiagramOfMe();
        //PApplet.main("_02_colors.VennDiagram.VennDiagramOfMe");
        PApplet.runSketch(new String[]{"Venn Diagram of Me"}, vdom);
    }

    @Override
    public void settings() {
        size(600, 600);
    }

    @Override
    public void setup() {
        System.out.println("Setup called");
        surface.setResizable(true); // Allow resizing to help with display issues
        surface.setLocation(10, 10); // Set a specific location for the window
   
    }


}
