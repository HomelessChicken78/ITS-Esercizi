package com.spring.pokemon.service;

import java.util.List;

import com.spring.pokemon.dto.PokemonDTO;

public interface PokemonService {
	public void registra(PokemonDTO dto);

	public PokemonDTO cercaPerId(int id);

	public List<PokemonDTO> cercaTutti();

	public void eliminaPerId(int id);
}
