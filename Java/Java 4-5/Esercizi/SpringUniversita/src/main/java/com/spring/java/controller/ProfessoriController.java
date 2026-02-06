package com.spring.java.controller;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.java.dto.DTOProfessore;
import com.spring.java.service.ProfessoriService;

@RestController
@RequestMapping(path = "/prof")
public class ProfessoriController {
	private ProfessoriService service = new ProfessoriService();

	@GetMapping(path = "/aggiungi", consumes = "application/json")
	public boolean aggiungi(@RequestBody DTOProfessore prof) {
		return service.aggiungiNuovoProfessore(prof);
	}

	@GetMapping(path = "/cercaPerId/{idProfessore}", produces = "application/json")
	public DTOProfessore cercaPerId(@PathVariable int idProfessore) {
		return service.cercaPerId(idProfessore);
	}

	@GetMapping(path = "/tutti", produces = "application/json")
	public List<DTOProfessore> visualizzaTutti() {
		return service.visualizzaTutti();
	}

	@GetMapping(path = "/cancella/{idProfessore}", produces = "application/json")
	public DTOProfessore cancella(@PathVariable int idProfessore) {
		return service.cancella(idProfessore);
	}

	@GetMapping(path = "/modificaMateria/{idProfessore}")
	public boolean modificaMateria(@PathVariable int idProfessore, String materia) {
		return service.modificaMateria(idProfessore, materia);
	}

	@GetMapping(path = "/insegnanoQuestaMateria", produces = "application/json")
	public List<DTOProfessore> insegnanoQuestaMateria(String materia) {
		return service.insegnanoMateria(materia);
	}

	@GetMapping(path = "/ordinaCognome", produces = "application/json")
	public List<DTOProfessore> ordinaCognome() {
		return service.ordinaCognome();
	}

	@GetMapping(path = "/materie", produces = "application/json")
	public List<String> materieInsegnate() {
		return service.visualizzaMaterie();
	}
}
