package com.spring.pokemon.mapper;

import com.spring.pokemon.dto.PokemonDTO;
import com.spring.pokemon.entity.Pokemon;

public class MapperConverter {
	// metodi statici di conversione
	public static Pokemon pokemonDTO2Entity(PokemonDTO dto) {
		return new Pokemon(dto.getId(), dto.getNome(), dto.getTipo());
	}

	public static PokemonDTO pokemonEntity2DTO(Pokemon entity) {
		return new PokemonDTO(entity.getId(), entity.getNome(), entity.getTipo());
	}
}
