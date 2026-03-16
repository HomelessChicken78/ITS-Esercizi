package com.spring.catalogo.listener;

import com.fasterxml.jackson.core.JsonProcessingException;

public interface ProductListener {
	void consume(String json) throws JsonProcessingException;
}
