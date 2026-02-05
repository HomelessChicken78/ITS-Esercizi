package com.spring.java.service;

import java.util.ArrayList;
import java.util.List;

import com.spring.java.dao.DAOUtenteMappa;
import com.spring.java.dto.NomiUtentiENumeroDTO;
import com.spring.java.dto.UtenteDTO;
import com.spring.java.entity.Utente;

public class UtenteService {

	private DAOUtenteMappa dao = new DAOUtenteMappa();
	public boolean registra(UtenteDTO dto) {
		Utente utente = new Utente();
		utente.setCognome(dto.getCognome());
		utente.setIdUtente(dto.getIdUtente());
		utente.setMail(dto.getMail());
		utente.setNome(dto.getNome());
		utente.setTelefono(dto.getTelefono());

		return dao.insert(utente);
	}

	public UtenteDTO cercaPerId(int idUtente) {
		// return dao.selectById(idUtente);
		Utente u = dao.selectById(idUtente);

		return new UtenteDTO(u.getNome(), u.getCognome(), u.getMail(), u.getTelefono(), u.getIdUtente());
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

	public NomiUtentiENumeroDTO getNomiNumeroUtenti() {
		List<Utente> lista = dao.selectAll();
		List<String> nomi = new ArrayList<>();

		for (Utente utente : lista)
			nomi.add(utente.getNome());

		return new NomiUtentiENumeroDTO(nomi, nomi.size());
	}
}
