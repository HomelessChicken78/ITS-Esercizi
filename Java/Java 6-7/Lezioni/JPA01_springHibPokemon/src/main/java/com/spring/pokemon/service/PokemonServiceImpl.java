package com.spring.pokemon.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.pokemon.dto.PokemonDTO;
import com.spring.pokemon.entity.Pokemon;
import com.spring.pokemon.mapper.MapperConverter;
import com.spring.pokemon.repository.DAOPokemon;

import jakarta.transaction.Transactional;

@Service
@Transactional
public class PokemonServiceImpl implements PokemonService {
	@Autowired
	private DAOPokemon dao;
	
	@Override
	public void registra(PokemonDTO dto) {
		Pokemon p = MapperConverter.pokemonDTO2Entity(dto);

		dao.save(p);
	}

	@Override
	public PokemonDTO cercaPerId(int id) {
		Optional<Pokemon> opt = dao.findById(id);
		if (opt.isPresent()) {
			Pokemon pokemonTrovato = opt.get();
			return MapperConverter.pokemonEntity2DTO(pokemonTrovato);
		}
		return null;
	}

	@Override
	public List<PokemonDTO> cercaTutti() {
		return dao.findAll()
				.stream()
				.map(p -> MapperConverter.pokemonEntity2DTO(p))
				.toList();
	}

	@Override
	public void eliminaPerId(int id) {
		dao.deleteById(id);
	}

}
