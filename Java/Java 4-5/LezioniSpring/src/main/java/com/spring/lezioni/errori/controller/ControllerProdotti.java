package com.spring.lezioni.errori.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.lezioni.errori.DuplicateIdException;
import com.spring.lezioni.errori.dto.ErrorDTO;
import com.spring.lezioni.errori.dto.ProductDTO;
import com.spring.lezioni.errori.service.ServiceProd;

@RestController
@RequestMapping(path = "/prodotti")
public class ControllerProdotti {
	@Autowired
	ServiceProd service;

	@GetMapping(path = "/add", consumes = "application/json")
	public void aggiungi(@RequestBody ProductDTO prod) {
		service.salvaProdotto(prod);
	}

	@GetMapping(path = "/cerca", produces = "application/json")
	public ProductDTO cerca(int id) {
		return service.cercaProdotto(id);
	}

	@ExceptionHandler
	public ResponseEntity<ErrorDTO> idProdDuplicate(DuplicateIdException err) {
		ErrorDTO returningError = new ErrorDTO();
		returningError.setMessage(err.getMessage());

		return new ResponseEntity<ErrorDTO>(returningError, HttpStatus.BAD_REQUEST);
	}

	@ExceptionHandler
	public ResponseEntity<ErrorDTO> second(DuplicateIdException err) {
		ErrorDTO returningError = new ErrorDTO();
		returningError.setMessage(err.getMessage());

		return new ResponseEntity<ErrorDTO>(returningError, HttpStatus.BAD_REQUEST);
	}
}
