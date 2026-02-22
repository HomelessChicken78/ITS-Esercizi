package com.spring.commerce.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.spring.commerce.dto.*;
import com.spring.commerce.service.ServiceVenditore;

@RestController
@RequestMapping(path = "/venditori")
public class VenditoreController {

	@Autowired
	private ServiceVenditore service;

	private static final String json = "application/json";

	@PostMapping(consumes = json, produces = json)
	public VenditoreDTO inserisciVenditore(@RequestBody VenditoreCreateRequestDTO dto) {
		return service.inserisciVenditore(dto);
	}

	@GetMapping(path = "/{idVenditore}", produces = json)
	public VenditoreDTO venditorePerId(@PathVariable int idVenditore) {
		return service.visualizzaPerId(idVenditore);
	}

	@GetMapping(path = "/{idVenditore}/base", produces = json)
	public VenditoreDatiBaseDTO visualizzaDatiVend(@PathVariable int idVenditore) {
		return service.visualizzaSemplificatoPerId(idVenditore);
	}

	@PatchMapping(path = "/{idVenditore}/password", consumes = json, produces = json)
	public VenditoreDTO modificaPasswordVenditore(@PathVariable int idVenditore, @RequestBody PasswordDTO nuovaPassword) {
		return service.modificaPassword(idVenditore, nuovaPassword.getPassword());
	}

	@PostMapping(path = "/{idVenditore}/prodotti", consumes = json)
	public ProdottoDTO aggiungiProdottoAdUnVenditore(@PathVariable int idVenditore, @RequestBody ProdottoDTO prodotto) {
		return service.aggiungiProdotto(idVenditore, prodotto);
	}

	@PatchMapping(path = "/{idVenditore}/prodotti/{idProdotto}", consumes = json, produces = json)
	public ProdottoDTO modificaQuantitaProdotto(@PathVariable int idVenditore, @PathVariable int idProdotto,
			@RequestBody QuantitaDTO nuovaQuantita) {
		return service.modificaQuantitaProdotto(idVenditore, idProdotto, nuovaQuantita.getQuantita());
	}
}