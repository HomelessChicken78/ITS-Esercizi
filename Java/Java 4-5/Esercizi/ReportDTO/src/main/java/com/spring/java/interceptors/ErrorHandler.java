package com.spring.java.interceptors;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import com.spring.java.dto.ErrorDTO;
import com.spring.java.exceptions.DuplicateIdException;
import com.spring.java.exceptions.IdNotFoundException;

@RestControllerAdvice
public class ErrorHandler {
	@ExceptionHandler
	public ResponseEntity<ErrorDTO> duplicateId(DuplicateIdException err) {
		return new ResponseEntity<ErrorDTO>(new ErrorDTO(err.getMessage()), HttpStatus.BAD_REQUEST);
	}

	@ExceptionHandler
	public ResponseEntity<ErrorDTO> notFound(IdNotFoundException err) {
		return new ResponseEntity<ErrorDTO>(new ErrorDTO(err.getMessage()), HttpStatus.NOT_FOUND);
	}
}
