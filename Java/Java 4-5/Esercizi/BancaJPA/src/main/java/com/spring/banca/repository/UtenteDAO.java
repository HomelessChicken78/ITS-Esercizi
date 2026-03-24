package com.spring.banca.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.spring.banca.entity.Utente;

public interface UtenteDAO extends JpaRepository<Utente, Integer> {

}
