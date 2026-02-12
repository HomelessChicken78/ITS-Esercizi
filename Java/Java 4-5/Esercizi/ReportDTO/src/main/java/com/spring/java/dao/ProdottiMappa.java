package com.spring.java.dao;

import java.util.List;

import com.spring.java.entity.Prodotto;

public interface ProdottiMappa {
    void insert(Prodotto utente);

    List<Prodotto> selectAll();

    Prodotto selectById(Integer idUtente);

    Prodotto delete(Integer idUtente);
}
