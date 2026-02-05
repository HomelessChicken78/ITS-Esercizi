package com.spring.java.dtoEsempio.controller;


import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.java.dtoEsempio.dto.NomiUtentiENumeroDTO;
import com.spring.java.dtoEsempio.dto.UtenteDTO;
import com.spring.java.dtoEsempio.entity.Utente;
import com.spring.java.dtoEsempio.service.UtenteService;



@RestController
@RequestMapping(path = "/utenti")
public class UtenteController {
	private UtenteService service = new UtenteService();

	@GetMapping(path = "/salva", consumes = "application/json")
	public boolean salva(@RequestBody UtenteDTO utente) {
		return service.registra(utente);
	}

	@GetMapping(path = "/cerca/{idUtente}", produces = "application/json")
	public UtenteDTO visualizza(@PathVariable int idUtente) {
		return service.cercaPerId(idUtente);
	}

	@GetMapping(path = "/nomiNumero", produces = "application/json")
	public NomiUtentiENumeroDTO getNomiNumeroUtenti() {
		return service.getNomiNumeroUtenti();
	}
}
