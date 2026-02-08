package com.spring.lezioni.dtoEsempio.service;

import java.util.ArrayList;
import java.util.List;

import com.spring.lezioni.dtoEsempio.dao.DAOUtenteMappa2;
import com.spring.lezioni.dtoEsempio.dto.NomiUtentiENumeroDTO2;
import com.spring.lezioni.dtoEsempio.dto.UtenteDTO2;
import com.spring.lezioni.dtoEsempio.entity.Utente2;




public class UtenteService2 {

	private DAOUtenteMappa2 dao = new DAOUtenteMappa2();
	public boolean registra(UtenteDTO2 dto) {
		Utente2 utente = new Utente2();
		utente.setCognome(dto.getCognome());
		utente.setIdUtente(dto.getIdUtente());
		utente.setMail(dto.getMail());
		utente.setNome(dto.getNome());
		utente.setTelefono(dto.getTelefono());

		return dao.insert(utente);
	}

	public UtenteDTO2 cercaPerId(int idUtente) {
		// return dao.selectById(idUtente);
		Utente2 u = dao.selectById(idUtente);

		return new UtenteDTO2(u.getNome(), u.getCognome(), u.getMail(), u.getTelefono(), u.getIdUtente());
	}

	public NomiUtentiENumeroDTO2 getNomiNumeroUtenti() {
		List<Utente2> lista = dao.selectAll();
		List<String> nomi = new ArrayList<>();

		for (Utente2 utente : lista)
			nomi.add(utente.getNome());

		return new NomiUtentiENumeroDTO2(nomi, nomi.size());
	}
}
