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
	private ServiceWriteProdotto service;

	@PostMapping(produces = json, consumes = json)
	@ResponseStatus(code = HttpStatus.CREATED)
	public ProdottoDTO aggiungiProdotto(@RequestBody ProdottoDTO nuovoProdotto) {
		return service.aggiungiProdotto(nuovoProdotto);
	}

	/*@DeleteMapping(path = "/{idProd}", produces = json)
	public ProdottoDTO eliminaProdotto(@PathVariable int idProd) {
		return service.eliminaProdotto(idProd);
	}*/

	@PutMapping(path = "/{idProd}/quantita", produces = json)
	public ProdottoDTO cambiaQuantita(@PathVariable int idProd, @RequestParam int nuovaQuantita) {
		return service.cambiaQuantita(idProd, nuovaQuantita);
	}
}