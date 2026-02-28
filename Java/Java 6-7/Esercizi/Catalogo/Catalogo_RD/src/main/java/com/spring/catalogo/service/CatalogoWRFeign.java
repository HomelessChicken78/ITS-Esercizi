package com.spring.catalogo.service;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.spring.catalogo.dto.ProdottoDTO;

@FeignClient("catalogo-WR")
public interface CatalogoWRFeign {
	@GetMapping(value = "/prodotti/{idProd}", produces = "application/json")
	ProdottoDTO getProdotto(@PathVariable int idProd);

	@GetMapping(value = "/prodotti/{idProd}/versione", produces = "application/json")
	Integer getVersion(@PathVariable int idProd);
}
