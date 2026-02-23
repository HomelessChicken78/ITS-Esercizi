package com.spring.azienda.dao;

import org.springframework.data.jpa.repository.JpaRepository;

import com.spring.azienda.entity.Azienda;

public interface AziendaDAO extends JpaRepository<Azienda, Integer> {

}
