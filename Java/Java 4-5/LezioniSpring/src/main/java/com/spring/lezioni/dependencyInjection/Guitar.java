package com.spring.lezioni.dependencyInjection;

import org.springframework.stereotype.Component;

@Component
public class Guitar implements Instrument {
	@Override
	public void play() {
		System.out.println("I'm playing drums.");
	}
}
