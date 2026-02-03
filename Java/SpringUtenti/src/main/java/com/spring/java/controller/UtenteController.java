package com.spring.java.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.java.entity.Utente;
import com.spring.java.service.UtenteService;

@RestController
@RequestMapping(path = "/utenti")
public class UtenteController {
	private UtenteService service = new UtenteService();

	@GetMapping(path = "/salva", consumes = "application/json")
	public boolean salva(@RequestBody Utente utente) {
		return service.registra(utente);
	}

	@GetMapping(path = "/cerca/{idUtente}", produces = "application/json")
	public Utente visualizza(@PathVariable int idUtente) {
		return service.cercaPerId(idUtente);
	}
}
