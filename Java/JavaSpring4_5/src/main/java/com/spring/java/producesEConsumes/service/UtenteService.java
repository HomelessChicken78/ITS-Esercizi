package com.spring.java.producesEConsumes.service;

import com.spring.java.producesEConsumes.entity.Utente;

public class UtenteService {
	// metodo di registrazione FAKE
	public boolean registra(Utente utente) {
		System.out.println("registrazione avvenuta: " + utente);
		return true;
	}

	public Utente cercaPerId(int idUtente) {
		return new Utente("mario", "rossi", "red@gmail.com", "112233", idUtente);
	}
}
