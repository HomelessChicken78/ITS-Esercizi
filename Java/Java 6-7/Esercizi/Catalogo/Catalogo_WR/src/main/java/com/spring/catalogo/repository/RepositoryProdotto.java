package com.spring.catalogo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.spring.catalogo.entity.Prodotto;

public interface RepositoryProdotto extends JpaRepository<Prodotto, Integer> {

}
