package com.spring.lezioni.dependencyInjection;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;@SuppressWarnings("unused")

//Here we have two type of creation:
// 1. @Component as comment, because we can't have two components in implemented class
// 2. Using the @Primary to flag the class as the priority one
// @Component
@Primary // Senza questo si arrabbia
public class Drums implements Instrument {
	@Override 
	public void play() {
		System.out.println("I'm playing the guitar.");
	}
}
