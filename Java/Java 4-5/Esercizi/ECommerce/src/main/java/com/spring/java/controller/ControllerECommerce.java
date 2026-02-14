package com.spring.java.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.spring.java.dto.OrderCreateRequestDTO;
import com.spring.java.dto.OrderResponseDTO;
import com.spring.java.service.OrderService;

@RequestMapping(path = "/orders")
@RestController
public class ControllerECommerce {
	@Autowired
	OrderService service;

	@ResponseStatus(code = HttpStatus.CREATED)
	@PostMapping(consumes = "application/json", produces = "application/json")
	public OrderResponseDTO createNewOrder(@RequestBody OrderCreateRequestDTO newOrd) {
		return service.createOrder(newOrd);
	}

	@ResponseStatus(code = HttpStatus.CREATED)
	@PostMapping(path = "/bulk", consumes = "application/json", produces = "application/json")
	public List<OrderResponseDTO> createNewOrder(@RequestBody List<OrderCreateRequestDTO> listOrds) {
		return service.createListOrders(listOrds);
	}

	@GetMapping(path = "{orderId}", produces = "application/json")
	public OrderResponseDTO searchOrderById(@PathVariable int orderId) {
		return service.searchOrderById(orderId);
	}
}
