package com.spring.commerce.service;

import org.springframework.stereotype.Service;

import com.spring.commerce.dto.*;

public interface ServiceVenditore {
	public VenditoreDTO inserisciVenditore(VenditoreCreateRequestDTO nuovoVenditore);

	public VenditoreDTO visualizzaPerId(int idVenditore);

	public VenditoreDatiBaseDTO visualizzaSemplificatoPerId(int idVenditore);

	public VenditoreDTO modificaPassword(int idVenditore, String nuovaPassword);

	public ProdottoDTO aggiungiProdotto(int idVenditore, ProdottoDTO nuovoProdotto);

	public ProdottoDTO modificaQuantitaProdotto(int idVenditore, int idProdotto, int nuovaQuantita);
}