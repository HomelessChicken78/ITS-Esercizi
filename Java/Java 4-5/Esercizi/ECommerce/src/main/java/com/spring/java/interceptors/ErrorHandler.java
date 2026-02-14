package com.spring.java.interceptors;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import com.spring.java.dto.ErrorDTO;
import com.spring.java.exception.ConflictException;
import com.spring.java.exception.InvalidFieldException;
import com.spring.java.exception.NotFoundException;

@RestControllerAdvice
public class ErrorHandler {
	@ExceptionHandler
	public ResponseEntity<ErrorDTO> notFoundHandler(NotFoundException err404) {
		ErrorDTO json = new ErrorDTO(404, err404.getMessage());
		return new ResponseEntity<ErrorDTO>(json, HttpStatus.NOT_FOUND);
	}

	@ExceptionHandler
	public ResponseEntity<ErrorDTO> conflictHandler(ConflictException err409) {
		ErrorDTO json = new ErrorDTO(409, err409.getMessage());
		return new ResponseEntity<ErrorDTO>(json, HttpStatus.CONFLICT);
	}

	@ExceptionHandler
	public ResponseEntity<ErrorDTO> invalidQueryStringHandler(InvalidFieldException err400) {
		ErrorDTO json = new ErrorDTO(400, err400.getMessage());
		return new ResponseEntity<ErrorDTO>(json, HttpStatus.BAD_REQUEST);
	}
}