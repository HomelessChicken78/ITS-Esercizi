package com.spring.java.dao;

import java.util.List;

import com.spring.java.entity.Utente;

public interface DAOUtenteMappa {
    void insert(Utente utente);

    List<Utente> selectAll();

    Utente selectById(Integer idUtente);

    Utente delete(Integer idUtente);
}