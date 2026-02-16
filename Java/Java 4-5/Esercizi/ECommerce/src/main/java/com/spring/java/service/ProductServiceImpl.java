package com.spring.java.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.java.dao.ProductManager;
import com.spring.java.dto.ProductAndCredentialsDTO;
import com.spring.java.dto.ProductResponseDTO;
import com.spring.java.entity.AccessCredentials;
import com.spring.java.entity.Product;

@Service
public class ProductServiceImpl implements ProductService {
	@Autowired
	ProductManager dao;

	public static Product productDTO2Entity(ProductAndCredentialsDTO dto) {
	    if (dto == null)
	        return null;

		Product entity = new Product();
		entity.setId(dto.getId());
		entity.setName(dto.getName());
		entity.setPrice(dto.getPrice());
		entity.setStock(dto.getStock());

		return entity;
	}

	public static ProductResponseDTO productEntity2DTO(Product entity) {
		if (entity == null && entity == null)
			return null;

		ProductResponseDTO dto = new ProductResponseDTO();
		dto.setId(entity.getId());
		dto.setName(entity.getName());
		dto.setPrice(entity.getPrice());
		dto.setStock(entity.getStock());

		return dto;
	}

	@Override
	public void addProduct(ProductAndCredentialsDTO prodAndCredentials) {
		dao.insert(productDTO2Entity(prodAndCredentials));
	}

	@Override
	public ProductResponseDTO getProductById(int idProd) {
		return productEntity2DTO(dao.selectById(idProd));
	}

	@Override
	public List<ProductResponseDTO> getAllProducts() {
		return dao.findAll()
				.stream()
				.map(prod -> productEntity2DTO(prod))
				.toList();
	}
}
