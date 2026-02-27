package com.spring.catalogo.controller;

import com.spring.catalogo.dto.*;
import com.spring.catalogo.service.*;
import org.springframework.beans.factory.annotation.*;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/prodotti")
public class ProdottoController {
	@Autowired
	private ServiceWriteProdotto service;

	@PostMapping
	@ResponseStatus(code = HttpStatus.CREATED)
	public ProdottoDTO aggiungiProdotto(@RequestBody ProdottoDTO nuovoProdotto) {
		return service.aggiungiProdotto(nuovoProdotto);
	}

	@DeleteMapping("/{idProd}")
	public ProdottoDTO eliminaProdotto(@PathVariable int idProd) {
		return service.eliminaProdotto(idProd);
	}

	@PutMapping("/{idProd}/quantita")
	public ProdottoDTO cambiaQuantita(@PathVariable int idProd, @RequestParam int nuovaQuantita) {
		return service.cambiaQuantita(idProd, nuovaQuantita);
	}

	@GetMapping("/{idProd}")
	public ProdottoDTO getProdotto(@PathVariable int idProd) {
		return service.getProdotto(idProd);
	}

	@GetMapping("/{idProd}/versione")
	public Integer getVersion(@PathVariable int idProd) {
		return service.getVersion(idProd);
	}
}