package com.spring.java.controller;


import java.util.List;

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

	@GetMapping(path = "/cancella/{idUtente}", produces = "application/json")
	public Utente cancellaUtente(@PathVariable int idUtente) {
		return service.eliminaUtente(idUtente);
	}

	@GetMapping(path = "/listaCompleta", produces = "application/json")
	public List<Utente> listaCompletaUtenti() {
		return service.listaUtenti();
	}

	@GetMapping(path = "/aggiornaEmail/{idUtente}", produces = "application/json")
	public Utente changeEmail(@PathVariable int idUtente, String mail) {
		return service.aggiornaEmail(idUtente, mail);
	}

	@GetMapping(path = "/numeroUtenti")
	public int getNumeroUtenti() {
		return service.getNumeroUtenti();
	}

	@GetMapping(path = "/listaNomi")
	public List<String> getListaNomi() {
		return service.getNomiUtenti();
	}

	@GetMapping(path = "/cercaNome", produces = "application/json")
	public List<Utente> cercaUtentiPerNome(String nome) {
		return service.cercaPerNome(nome);
	}
}
