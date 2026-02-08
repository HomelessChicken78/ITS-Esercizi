package com.spring.lezioni.producesEConsumes.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.lezioni.producesEConsumes.entity.Utente2;
import com.spring.lezioni.producesEConsumes.service.UtenteService2;

@RestController
@RequestMapping(path = "/utenti2")
public class UtenteController2 {
	private UtenteService2 service = new UtenteService2();

	@GetMapping(path = "/salva", consumes = "application/json")
	public boolean salva(@RequestBody Utente2 utente) {
		return service.registra(utente);
	}

	@GetMapping(path = "/cerca/{idUtente}", produces = "application/json")
	public Utente2 visualizza(@PathVariable int idUtente) {
		return service.cercaPerId(idUtente);
	}
}
