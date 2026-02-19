package com.spring.impiegati.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.spring.impiegati.entity.Impiegato;

public interface RepositoryImpiegati extends JpaRepository<Impiegato, String> {
	@Query(nativeQuery = true, value = "SELECT * FROM impiegato ORDER BY cognome")
	public List<Impiegato> ordinaPerCognome();

	@Query(nativeQuery = true, value = "SELECT * FROM impiegato ORDER BY matricola")
	public List<Impiegato> ordinaPerMatricola();
}
