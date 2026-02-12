package com.spring.lezioni.errori.dao;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.spring.lezioni.errori.DuplicateIdException;
import com.spring.lezioni.errori.NotFoundException;
import com.spring.lezioni.errori.entity.Product;


@Repository
public class ProductDAO {
    private Map<Integer, Product> mappa = new HashMap<>();

    public void insert(Product prod) {
        if(mappa.containsKey(prod.getProdId()))
            throw new DuplicateIdException("Duplicate id!");

        mappa.put(prod.getProdId(), prod);
    }

    public Product selectById(Integer idProd) {
        Product prod = mappa.get(idProd);
        if(prod == null)
            throw new NotFoundException("Id " + idProd + " doesn't exist");
        else
            return prod;
    }
}
