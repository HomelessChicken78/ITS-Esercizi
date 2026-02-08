package com.spring.lezioni.dtoEsempio.service;

import java.util.ArrayList;
import java.util.List;

import com.spring.lezioni.dtoEsempio.dao.DAOUtenteMappa;
import com.spring.lezioni.dtoEsempio.dto.NomiUtentiENumeroDTO;
import com.spring.lezioni.dtoEsempio.dto.UtenteDTO;
import com.spring.lezioni.dtoEsempio.entity.Utente;




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

	public NomiUtentiENumeroDTO getNomiNumeroUtenti() {
		List<Utente> lista = dao.selectAll();
		List<String> nomi = new ArrayList<>();

		for (Utente utente : lista)
			nomi.add(utente.getNome());

		return new NomiUtentiENumeroDTO(nomi, nomi.size());
	}
}
