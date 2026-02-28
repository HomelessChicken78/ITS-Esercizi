package com.spring.catalogo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.spring.catalogo.dto.ProdottoDTO;
import com.spring.catalogo.service.ServiceProdotto;

@RestController
@RequestMapping("/prodotti")
public class ProdottiController {
	private static final String json = "application/json";

	@Autowired
	private ServiceProdotto service;

	@GetMapping(path = "/{idProd}", produces = json)
	public ProdottoDTO getProdotto(@PathVariable int idProd) {
		return service.getProdotto(idProd);
	}
}
