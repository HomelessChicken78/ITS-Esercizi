package com.spring.commerce.interceptors;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.spring.commerce.dto.ErrorDTO;
import com.spring.commerce.exceptions.NotFoundException;

@RestControllerAdvice
public class GlobalExceptionHandler {
	@ExceptionHandler
	public ResponseEntity<ErrorDTO> NotFoundHandler(NotFoundException err404) {
		return new ResponseEntity<ErrorDTO>(new ErrorDTO(err404.getMessage(), 404), HttpStatus.NOT_FOUND);
	}
}
