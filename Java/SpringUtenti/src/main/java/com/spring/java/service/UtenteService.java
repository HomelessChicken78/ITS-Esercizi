package com.spring.java.service;

import java.util.ArrayList;
import java.util.List;

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

	public List<Utente> listaUtenti() {
		return dao.selectAll();
	}

	public Utente eliminaUtente(int idUtente) {
		return dao.delete(idUtente);
	}

	public Utente aggiornaEmail(int idUtente, String nuovaEmail) {
		if (cercaPerId(idUtente) == null)
			return null;
		Utente utenteCancellato = dao.delete(idUtente);
		utenteCancellato.setMail(nuovaEmail);
		dao.insert(utenteCancellato);
		return utenteCancellato;
	}

	public int getNumeroUtenti() {
		return dao.selectAll().size();
	}

	public List<String>  getNomiUtenti() {
		ArrayList<String> res = new ArrayList<>();

		for (Utente ut : dao.selectAll())
			res.add(ut.getNome());

		return res;
	}

	public List<Utente> cercaPerNome(String nome) {
		ArrayList<Utente> res = new ArrayList<>();

		for (Utente ut : dao.selectAll())
			if (ut.getNome().equals(nome))
				res.add(ut);

		return res;
	}
}
