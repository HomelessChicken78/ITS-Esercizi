package com.spring.catalogo.interceptors;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import com.spring.catalogo.dto.ErrorDTO;
import com.spring.catalogo.exceptions.*;

@RestControllerAdvice
public class GlobalExceptionHandlers {
	@ExceptionHandler
	public ResponseEntity<ErrorDTO> notFoundHandler(NotFoundException err404) {
		return new ResponseEntity<>(new ErrorDTO(err404.getMessage()), HttpStatus.NOT_FOUND);
	}
}
