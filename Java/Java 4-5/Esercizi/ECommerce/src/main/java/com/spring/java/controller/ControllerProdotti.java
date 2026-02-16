package com.spring.java.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.spring.java.dto.ProductAndCredentialsDTO;
import com.spring.java.dto.ProductResponseDTO;
import com.spring.java.service.ProductService;

@RestController
@RequestMapping(path = "/products")
public class ControllerProdotti {
	@Autowired
	ProductService service;

	@ResponseStatus(HttpStatus.CREATED)
	@PostMapping(consumes = "application/json")
	public void addProduct(@RequestBody ProductAndCredentialsDTO prod) {
		service.addProduct(prod);
	}

	@GetMapping()
	public List<ProductResponseDTO> getAllProducts() {
		return service.getAllProducts();
	}

	@GetMapping(path = "/{idProd}")
	public ProductResponseDTO getProduct(@PathVariable int idProd) {
		return service.getProductById(idProd);
	}
}
