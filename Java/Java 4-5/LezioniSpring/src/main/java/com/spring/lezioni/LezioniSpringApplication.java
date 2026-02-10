package com.spring.lezioni;

import com.spring.lezioni.aop.entity.Artista;
import com.spring.lezioni.dependencyInjection.MusicPlayer;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class LezioniSpringApplication {
	public static void main(String[] args) {
		ApplicationContext context = SpringApplication.run(LezioniSpringApplication.class, args);

		MusicPlayer mplr = context.getBean(MusicPlayer.class);

		mplr.playInstrument();

		Artista art = context.getBean(Artista.class);
		art.setNome("Stefano Reali");

		art.perform();
	}
}
