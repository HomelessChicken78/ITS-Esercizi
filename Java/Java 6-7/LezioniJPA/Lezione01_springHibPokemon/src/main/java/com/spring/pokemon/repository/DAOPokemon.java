package com.spring.pokemon.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.spring.pokemon.entity.Pokemon;

public interface DAOPokemon extends JpaRepository<Pokemon, Integer> {
	// qui eredito soltanto i metodi del JPA repository
}
