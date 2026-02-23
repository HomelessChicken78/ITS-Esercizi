package com.spring.azienda.service;

import java.util.Collection;

import com.spring.azienda.dto.*;

public interface AziendaService {
	public AziendaDTO inserisciNuova(AziendaDTO azienda);

	public AziendaDTO visualizzaDati(int idAzienda);

	public AziendaDatiBaseDTO visualizzaDatiBase(int idAzienda);

	public Collection<AziendaDTO> visualizzaTutte();

	public AziendaDatiBaseAndNumeroDipendentiDTO visualizzaDatiBaseENumeroDipendenti(int idAzienda);
}
