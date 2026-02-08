package com.spring.lezioni.producesEConsumes.service;

import com.spring.lezioni.producesEConsumes.entity.Utente2;

public class UtenteService2 {
	// metodo di registrazione FAKE
	public boolean registra(Utente2 utente) {
		System.out.println("registrazione avvenuta: " + utente);
		return true;
	}

	public Utente2 cercaPerId(int idUtente) {
		return new Utente2("mario", "rossi", "red@gmail.com", "112233", idUtente);
	}
}
