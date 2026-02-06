package com.spring.java.controller;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.java.dto.DTOCognomeAnnoIscrizione;
import com.spring.java.dto.DTOCognomeAnnoNascita;
import com.spring.java.dto.DTOStudente;
import com.spring.java.service.StudentiService;

@RestController
@RequestMapping(path = "/stud")
public class StudentiController {
	private StudentiService service = new StudentiService();

	@GetMapping(path = "/aggiungi", consumes = "application/json")
	public boolean aggiungi(@RequestBody DTOStudente stud) {
		return service.aggiungiNuovoStudente(stud);
	}

	@GetMapping(path = "/cercaPerMatricola/{matricolaStud}", produces = "application/json")
	public DTOStudente cercaPerMatricola(@PathVariable int matricolaStud) {
		return service.cercaPerMatricola(matricolaStud);
	}

	@GetMapping(path = "/tutti", produces = "application/json")
	public List<DTOStudente> tutti() {
		return service.visualizzaTutti();
	}

	@GetMapping(path = "/cancella/{matricolaStud}", produces = "application/json")
	public DTOStudente cancella(@PathVariable int matricolaStud) {
		return service.cancella(matricolaStud);
	}

	@GetMapping(path = "/modificaIndirizzo/{matricolaStud}")
	public boolean modificaIndirizzo(@PathVariable int matricolaStud, String indirizzo) {
		return service.modificaIndirizzo(matricolaStud, indirizzo);
	}

	@GetMapping(path = "/tuttiNomi", produces = "application/json")
	public List<String> tuttiNomi() {
		return service.elencoNomi();
	}

	@GetMapping(path = "/piuGiovane", produces = "application/json")
	public DTOCognomeAnnoNascita piuGiovane() {
		return service.studPiuGiovane();
	}

	@GetMapping(path = "/iscrittoPiuTempo", produces = "application/json")
	public DTOCognomeAnnoIscrizione iscrittoPiuTempo() {
		return service.studIscrittoPiuTempo();
	}
}
