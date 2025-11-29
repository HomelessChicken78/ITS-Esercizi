package java1.classi.esercizi;

import java.util.Date;

import java.util.Scanner;

public class DateDifference {
	public static void main(String[] args) {
		/*
		 * Write a Java class with a main method that calculates the hours and minutes
		 * remaining until the end of class.
		 * 
		 * Version 1: Assume that class ends at 6:00 PM.
		 * Version 2: Allow the user to enter the end time
		 * (acquiring the hours and minutes with two separate
		 * readings).
		 * 
		 * Note: Use two objects of type java.util.Date.
		 */
		
		// First version
		Date now = new Date();
		System.out.println(now);
		
		Date endClass = new Date(now.getYear(), now.getMonth(), now.getDate(), 18, 0, 0);
		
        int hoursLeft = endClass.getHours() - now.getHours();
        int minutesLeft = endClass.getMinutes() - now.getMinutes();
        int secondsLeft = endClass.getSeconds() - now.getSeconds();
        
        // System.out.println(hoursLeft);
        // System.out.println(minutesLeft);
        // System.out.println(secondsLeft);
		
        if (secondsLeft < 0) {
        	minutesLeft--;
        	secondsLeft += 60;
        }
        if (minutesLeft < 0) {
        	hoursLeft--;
        	minutesLeft += 60;
        }
        
        if (hoursLeft < 0) {
        	System.out.println("The class has already finished!");
        } else {
        	System.out.println("Still " + hoursLeft + " hours, " + minutesLeft + " minutes and " + secondsLeft + " seconds left until the end of the class at 18:00.");
        }
        
        // Second version
        System.out.println();
        Scanner scan = new Scanner(System.in);
        int inputHours;
        int inputMinutes;
        do {
        	System.out.print("Insert the hour: -> ");
        	inputHours = scan.nextInt();
        	
        	if (inputHours < 0) {
        		System.out.println("Error: Insert a positive number!");
        	}
        } while (inputHours < 0);
        
        do {
        	System.out.print("Insert the minute: -> ");
        	inputMinutes = scan.nextInt();
        	
        	if (inputMinutes< 0) {
        		System.out.println("\nError: Insert a positive number!");
        	}
        } while (inputMinutes < 0);
        
		Date endTime = new Date(now.getYear(), now.getMonth(), now.getDate(), inputHours, inputMinutes, 0);
		
        int hoursLeft2 = endTime.getHours() - now.getHours();
        int minutesLeft2 = endTime.getMinutes() - now.getMinutes();
        int secondsLeft2 = endTime.getSeconds() - now.getSeconds();
		
        if (secondsLeft2 < 0) {
        	minutesLeft2--;
        	secondsLeft2 += 60;
        }
        if (minutesLeft2 < 0) {
        	hoursLeft2--;
        	minutesLeft2 += 60;
        }
        
        if (hoursLeft2 < 0) {
        	System.out.println("The class has already finished!");
        } else {
        	System.out.println("Still " + hoursLeft2 + " hours, " + minutesLeft2 + " minutes and " + secondsLeft2 + " seconds left until the end of the class.");
        }
	}
}
