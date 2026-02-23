package com.spring.azienda.service;

import java.util.Collection;

import com.spring.azienda.dto.*;

public interface AziendaService {
	public AziendaDTO inserisciNuova(AziendaDTO azienda);

	public AziendaDTO visualizzaDati(int idAzienda);

	public AziendaDatiBaseDTO visualizzaDatiBase(int idAzienda);

	public Collection<AziendaDTO> visualizzaTutte();

	public AziendaDatiBaseAndNumeroDipendentiDTO aziendaConPiuCapitaleSociale();

	public AziendaDatiBaseDTO modificaCapitaleSociale(int idAzienda, double nuovoCapitaleSociale);

	public AziendaDatiBaseDTO modificaIntestazione(int idAzienda, String nuovaIntestazione);

	public AziendaDTO cancellaAzienda(int idAzienda);

	public DipendenteDTO inserisciDipendente(int idAzienda, DipendenteDTO dipendente);

	public DipendenteDTO inserisciDipendente(int idAzienda, DipendenteDTO dipendente, PostoAutoDTO postoAuto);

	public DipendenteDTO inserisciDipendente(int idAzienda, DipendenteDTO dipente, int idPostoAuto);

	public Collection<DipendenteDTO> visualizzaTuttiDipendenti(int idAzienda);

	public Collection<NominativoDipendente> visualizzaNominativi(int idAzienda);

	public Collection<DipendenteDTO> ricercaPerSalario(int idAzienda, double salario);

	public DipendenteDTO cancellaPerMatricola(int idAzienda, String matricolaImpiegato);

	public NominativoDipendente cancellaPerMatricolaSoloNominativo(int idAzienda, String matricolaImpiegato);

	public SpostamentoDipendente spostaDipendente(int idAziendaVecchia, String matricolaImpiegato, int idAziendaNuova);
}
