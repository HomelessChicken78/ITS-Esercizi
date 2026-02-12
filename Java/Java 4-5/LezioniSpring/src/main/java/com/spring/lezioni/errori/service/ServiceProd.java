package com.spring.lezioni.errori.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.lezioni.errori.dao.ProductDAO;
import com.spring.lezioni.errori.dto.ProductDTO;
import com.spring.lezioni.errori.entity.Product;

@Service
public class ServiceProd {
	@Autowired
	ProductDAO dao;

	public void salvaProdotto(ProductDTO prod) {
		dao.insert(new Product(prod.getProdId(), prod.getName()));
	}

	public ProductDTO cercaProdotto(int idProd) {
		Product res = dao.selectById(idProd);

		return new ProductDTO(res.getProdId(), res.getName());
	}
}
