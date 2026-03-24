package com.spring.banca.service;

import java.util.Collection;

import com.spring.banca.dto.*;

public interface ServiceUtente {
	public UtenteDTO registraUtente(RegistraUtenteDTO nuovoUtente);
	public UtenteDTO modificaDati(int idUtente, UtenteDTO modificheUtente);
	public UtenteDTO cercaUtente(int idUtente);
	public UtenteConDatiSalienteDTO cercaUtenteDatiSalienti(int idUtente);
	public Collection<UtenteConResidenzaDTO> reportUtenti();
	public void cancellaUtente(int idUtente);
}
