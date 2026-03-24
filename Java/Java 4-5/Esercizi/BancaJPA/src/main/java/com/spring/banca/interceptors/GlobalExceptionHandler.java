package com.spring.banca.interceptors;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import com.spring.banca.dto.ErrorDTO;
import com.spring.banca.exceptions.NotFoundException;

@RestControllerAdvice
public class GlobalExceptionHandler {
	@ExceptionHandler
	public ResponseEntity<ErrorDTO> notFoundHandler(NotFoundException error404) {
		return new ResponseEntity<ErrorDTO>(new ErrorDTO(error404.getMessage(), 404), HttpStatus.NOT_FOUND);
	}
}
