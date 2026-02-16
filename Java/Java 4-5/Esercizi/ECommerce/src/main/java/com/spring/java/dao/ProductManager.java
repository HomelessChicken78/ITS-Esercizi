package com.spring.java.dao;

import java.util.List;

import com.spring.java.entity.AccessCredentials;
import com.spring.java.entity.Product;

public interface ProductManager {
	public void insert(Product prod);

	public Product selectById(int idProd);

	public int selectStockById(int idProd);

	public void updateStockById(int idProd, int newStock);

	public List<Product> findAll();
}
