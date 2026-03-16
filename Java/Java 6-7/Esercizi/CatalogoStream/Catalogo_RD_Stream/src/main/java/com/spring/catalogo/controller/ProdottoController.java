package com.spring.catalogo.controller;

import com.spring.catalogo.dto.*;
import com.spring.catalogo.service.*;
import org.springframework.beans.factory.annotation.*;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/prodotti")
public class ProdottoController {
	private static final String json = "application/json";
	@Autowired
	private ServiceReadProdotto service;

	@GetMapping(path = "/{idProd}", produces = json)
	public ProdottoDTO getProdotto(@PathVariable int idProd) {
		return service.getProdotto(idProd);
	}
}