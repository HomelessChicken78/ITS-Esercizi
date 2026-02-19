package com.spring.impiegati.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.spring.impiegati.entity.Impiegato;

public interface RepositoryImpiegati extends JpaRepository<Impiegato, String> {
	
}
