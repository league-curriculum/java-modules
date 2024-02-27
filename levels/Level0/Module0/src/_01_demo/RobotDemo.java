package _01_demo;

/*
 *    Copyright (c) The League of Amazing Programmers 2013-2020
 *    Level 0
 */

import org.jointheleague.graphical.robot.Robot;

// This recipe draws a square using the Robot

public class RobotDemo {

	public static void main(String[] args) {

		// This code makes a new Robot
		Robot rob = new Robot();

		// PEN. Put the robot's pen down so it can draw, Use this command:
		rob.penDown();

		// SPEED. Make the robot move quickly. Use this command:
		rob.setSpeed(100);

		for(int i = 0; i < 40; i++){
			rob.move(200);
			rob.turn(70);
		}

	}
}
