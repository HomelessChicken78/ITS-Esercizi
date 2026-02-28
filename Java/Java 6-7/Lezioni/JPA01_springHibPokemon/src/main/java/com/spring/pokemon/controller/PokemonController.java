package com.spring.pokemon.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.pokemon.dto.PokemonDTO;
import com.spring.pokemon.service.PokemonService;

@RestController
@RequestMapping(path = "/pokemon")
public class PokemonController {
	@Autowired
	private PokemonService service;

	@PostMapping(consumes = "application/json")
	public void registra(@RequestBody PokemonDTO dto) {
		service.registra(dto);
	}

	@GetMapping(path = "/{id}", produces = "application/json")
	public PokemonDTO cercaPerId(@PathVariable int id) {
		return service.cercaPerId(id);
	}

	@GetMapping(produces = "application/json")
	public List<PokemonDTO> cercaTutti() {
		return service.cercaTutti();
	}

	@DeleteMapping(path = "/{id}")
	public void elimina(@PathVariable int id) {
		service.eliminaPerId(id);
	}

}
