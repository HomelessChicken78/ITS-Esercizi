package com.spring.impiegati.interceptors;

import org.springframework.web.bind.annotation.RestControllerAdvice;

import com.spring.impiegati.dto.ErrorDTO;
import com.spring.impiegati.exception.NotFoundException;
import com.spring.impiegati.service.SalarioInvalidoException;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;

@RestControllerAdvice
public class GlobalExceptionHandler {
	@ExceptionHandler
	public ResponseEntity<ErrorDTO> NotFoundHandler(NotFoundException err404) { 
		ErrorDTO responseDTO = new ErrorDTO(err404.getMessage(), 404);

		return new ResponseEntity<ErrorDTO>(responseDTO, HttpStatus.NOT_FOUND);
	}

	@ExceptionHandler
	public ResponseEntity<ErrorDTO> SalarioInvalidoHandler(SalarioInvalidoException err400) { 
		ErrorDTO responseDTO = new ErrorDTO(err400.getMessage());

		return new ResponseEntity<ErrorDTO>(responseDTO, HttpStatus.BAD_REQUEST);
	}
}
