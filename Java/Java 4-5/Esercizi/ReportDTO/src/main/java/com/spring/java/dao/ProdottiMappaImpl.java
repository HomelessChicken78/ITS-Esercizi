package com.spring.java.dao;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.spring.java.entity.Prodotto;
import com.spring.java.exceptions.DuplicateIdException;
import com.spring.java.exceptions.IdNotFoundException;

@Repository
public class ProdottiMappaImpl implements ProdottiMappa {

    private Map<Integer, Prodotto> mappa = new HashMap<>();

    public void insert(Prodotto prod) {
        if(mappa.containsKey(prod.getId()))
            throw new DuplicateIdException("Non è possibile creare due volte lo stesso prodotto con lo stesso ID !");

        mappa.put(prod.getId(), prod);
    }

    public List<Prodotto> selectAll(){
        return new ArrayList<>(mappa.values());
    }

    public Prodotto selectById(Integer idProd) {
    	Prodotto prod = mappa.get(idProd);
        if(prod == null)
            throw new IdNotFoundException("Non è stato possibile trovare un prodotto con ID " + idProd + " !");
        else
            return prod;
    }

    public Prodotto delete(Integer idProd) {
    	Prodotto prod = mappa.remove(idProd);
        if(prod == null)
            throw new IdNotFoundException("ID " + idProd + " non trovato !");
        else
            return prod;
    }
}