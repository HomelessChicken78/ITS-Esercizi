package com.spring.banca.controller;

import com.spring.banca.dto.UtenteDTO;
import com.spring.banca.service.ServiceUtente;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/utenti")
public class UtenteController {
	private static final String json = "application/json";

	@Autowired
	private ServiceUtente service;

	@ResponseStatus(HttpStatus.CREATED)
	@PostMapping(produces = json, consumes = json)
	public UtenteDTO registra(@RequestBody UtenteDTO nuovoUtente) {
		return service.registraUtente(nuovoUtente);
	}
}