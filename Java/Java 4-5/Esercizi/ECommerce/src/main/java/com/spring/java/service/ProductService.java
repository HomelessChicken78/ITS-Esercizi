package com.spring.java.service;

import java.util.List;

import com.spring.java.dto.ProductAndCredentialsDTO;
import com.spring.java.dto.ProductResponseDTO;

public interface ProductService {
	public void addProduct(ProductAndCredentialsDTO prodAndCredentials);

	public ProductResponseDTO getProductById(int idProd);

	public List<ProductResponseDTO> getAllProducts();
}
