package com.spring.java.dao;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.spring.java.entity.Utente;

@Repository
public class DAOUtenteMappaImpl implements DAOUtenteMappa {

    private Map<Integer, Utente> mappa = new HashMap<>();

    public void insert(Utente utente) {
        if(mappa.containsKey(utente.getIdUtente()))
            throw new RuntimeException("ERRORE: Non è possibile creare due volte lo stesso utente con lo stesso ID !");

        mappa.put(utente.getIdUtente(), utente);
    }

    public List<Utente> selectAll(){
        return new ArrayList<>(mappa.values());
    }

    public Utente selectById(Integer idUtente) {
        Utente utente = mappa.get(idUtente);
        if(utente == null)
            throw new RuntimeException("id utente non presente");
        else
            return utente;
    }

    public Utente delete(Integer idUtente) {
        Utente utente = mappa.remove(idUtente);
        if(utente == null)
            throw new RuntimeException("id utente non presente");
        else
            return utente;
    }
}