package com.spring.lezioni;

import com.spring.lezioni.dependencyInjection.MusicPlayer;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class LezioniSpringApplication {
	public static void main(String[] args) {
		ApplicationContext contex = SpringApplication.run(LezioniSpringApplication.class, args);

		MusicPlayer mplr = contex.getBean(MusicPlayer.class);

		mplr.playInstrument();
	}
}
