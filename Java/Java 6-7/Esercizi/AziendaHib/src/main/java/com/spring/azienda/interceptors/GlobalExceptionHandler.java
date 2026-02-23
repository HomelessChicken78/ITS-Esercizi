package com.spring.azienda.interceptors;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;

import com.spring.azienda.dto.ErrorDTO;
import com.spring.azienda.exceptions.*;

public class GlobalExceptionHandler {
	@ExceptionHandler
	public ResponseEntity<ErrorDTO> notFound(NotFoundException err404) {
		return new ResponseEntity<ErrorDTO>(new ErrorDTO(404, err404.getMessage()), HttpStatus.NOT_FOUND);
	}

	@ExceptionHandler
	public ResponseEntity<ErrorDTO> conflict(ConflictException err409) {
		return new ResponseEntity<ErrorDTO>(new ErrorDTO(409, err409.getMessage()), HttpStatus.CONFLICT);
	}

	@ExceptionHandler
	public ResponseEntity<ErrorDTO> badRequest(BadRequestException err400) {
		return new ResponseEntity<ErrorDTO>(new ErrorDTO(400, err400.getMessage()), HttpStatus.BAD_REQUEST);
	}
}
