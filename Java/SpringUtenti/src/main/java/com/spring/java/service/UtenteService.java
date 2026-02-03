package com.spring.java.service;

import com.spring.java.dao.DAOUtenteMappa;
import com.spring.java.entity.Utente;

public class UtenteService {

	private DAOUtenteMappa dao = new DAOUtenteMappa();
	// metodo di registrazione FAKE
	public boolean registra(Utente utente) {
		return dao.insert(utente);
	}

	public Utente cercaPerId(int idUtente) {
		return dao.selectById(idUtente);
	}
}
