package com.spring.lezioni.dtoEsempio.controller;


import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.lezioni.dtoEsempio.dto.NomiUtentiENumeroDTO2;
import com.spring.lezioni.dtoEsempio.dto.UtenteDTO2;
import com.spring.lezioni.dtoEsempio.service.UtenteService2;





@RestController
@RequestMapping(path = "/utenti2")
public class UtenteController2 {
	private UtenteService2 service = new UtenteService2();

	@GetMapping(path = "/salva", consumes = "application/json")
	public boolean salva(@RequestBody UtenteDTO2 utente) {
		return service.registra(utente);
	}

	@GetMapping(path = "/cerca/{idUtente}", produces = "application/json")
	public UtenteDTO2 visualizza(@PathVariable int idUtente) {
		return service.cercaPerId(idUtente);
	}

	@GetMapping(path = "/nomiNumero", produces = "application/json")
	public NomiUtentiENumeroDTO2 getNomiNumeroUtenti() {
		return service.getNomiNumeroUtenti();
	}
}
