package com.spring.lezioni.dependencyInjection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class MusicPlayer {

	@Autowired
	private Instrument instrument;

	public void playInstrument() {
		instrument.play();
	}
}
