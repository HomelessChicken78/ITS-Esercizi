package com.spring.impiegati.controller;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.spring.impiegati.dto.ImpiegatoDTO;
import com.spring.impiegati.dto.NomeAndCognomeImpiegatoDTO;
import com.spring.impiegati.dto.TotaleSalariDTO;
import com.spring.impiegati.service.ServiceImpiegato;

@RestController
@RequestMapping(value = "/impiegati", produces = "application/json")
public class ImpiegatoController {

	@Autowired
	private ServiceImpiegato service;

	@PostMapping(consumes = "application/json")
	@ResponseStatus(HttpStatus.CREATED)
	public void assumi(@RequestBody ImpiegatoDTO impiegato) {
		service.assumi(impiegato);
	}

	@GetMapping
	public List<ImpiegatoDTO> visualizzaTutti() {
		return service.visualizzaTutti();
	}

	@GetMapping(path = "/{matricola}")
	public ImpiegatoDTO cercaPerMatricola(@PathVariable String matricola) {
		return service.cercaPerMatricola(matricola);
	}

	@PatchMapping(path = "/{matricola}/salario")
	public ImpiegatoDTO modificaSalario(@PathVariable String matricola, double nuovoSalario) {
		return service.modificaSalario(matricola, nuovoSalario);
	}

	@DeleteMapping(path = "/{matricola}")
	public NomeAndCognomeImpiegatoDTO elimina(@PathVariable String matricola) {
		return service.eliminaPerMatricola(matricola);
	}

	@GetMapping(path = "/ordinaCognome")
	public List<ImpiegatoDTO> ordinaPerCognome() {
		return service.impiegatiOrdinatiPerCognome();
	}

	@GetMapping(path = "/ordinaMatricola")
	public List<NomeAndCognomeImpiegatoDTO> nomiAndCognomiOrdinati() {
		return service.nomiAndCognomiOrdinatiPerMatricola();
	}

	@GetMapping(path = "/totaleSalari")
	public TotaleSalariDTO getTotaleSalari() {
		return service.totaleSalariPagato();
	}

	@GetMapping(path = "/piuAnziano")
	public ImpiegatoDTO getAssuntoDaPiuTempo() {
		return service.assuntoDaPiuTempo();
	}

	@GetMapping(path = "/salarioPiuElevato")
	public ImpiegatoDTO getSalarioMaggioreDopoData(LocalDate data) {
		return service.salarioMaggioreDopoData(data);
	}
}