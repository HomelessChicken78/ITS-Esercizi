package com.spring.banca.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.banca.dto.RegistraUtenteDTO;
import com.spring.banca.dto.UtenteConDatiSalienteDTO;
import com.spring.banca.dto.UtenteConResidenzaDTO;
import com.spring.banca.dto.UtenteDTO;
import com.spring.banca.entity.Utente;
import com.spring.banca.repository.UtenteDAO;
import static com.spring.banca.utility.GenericMapper.*;
import static com.spring.banca.utility.UtenteMapper.*;

import java.util.Collection;

import jakarta.transaction.Transactional;

@Service
@Transactional
public class ServiceUtenteImpl implements ServiceUtente {
	@Autowired
	private UtenteDAO dao;

	private UtenteDTO findOrNull(int idUtente) {
		return toDTO(dao.findById(idUtente).orElse(null));
	}

	@Override
	public UtenteDTO registraUtente(RegistraUtenteDTO nuovoUtente) {
		Utente registrato = dao.save(toEntity(nuovoUtente));

		return toDTO(registrato);
	}

	@Override
	public UtenteDTO modificaDati(int idUtente, UtenteDTO modificheUtente) {
		Utente modificato = dao.save(toEntity(modificheUtente));

		return toDTO(modificato);
	}

	@Override
	public UtenteDTO cercaUtente(int idUtente) {
		return findOrNull(idUtente);
	}

	@Override
	public UtenteConDatiSalienteDTO cercaUtenteDatiSalienti(int idUtente) {
		UtenteConDatiSalienteDTO trovato = toDatiSalienti(findOrNull(idUtente));

		// TODO incompleta -> mancano conti
		return null;
	}

	@Override
	public Collection<UtenteConResidenzaDTO> reportUtenti() {
		// TODO Non fattibile -> manca l'indirizzo
		return null;
	}

	@Override
	public void cancellaUtente(int idUtente) {
		// TODO Non fattibile -> manca controllare i conti
	}
}
