package com.spring.java.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.spring.java.dto.ReportDTO;
import com.spring.java.service.Calcolatrice;
import com.spring.java.service.Report;

@RestController
public class CalcolatriceController {
	@Autowired
	private Calcolatrice service1;

	@Autowired
	private Report service2;

	@GetMapping(path = "/add/{n1}/{n2}")
	public int add(@PathVariable int n1, @PathVariable int n2) {
		return service1.add(n1, n2);
	}

	@GetMapping(path = "/subtract/{n1}/{n2}")
	public int subtract(@PathVariable int n1, @PathVariable int n2) {
		return service1.subtract(n1, n2);
	}

	@GetMapping(path = "/multiply/{n1}/{n2}")
	public int multiply(@PathVariable int n1, @PathVariable int n2) {
		return service1.multiply(n1, n2);
	}

	@GetMapping(path = "/divide/{n1}/{n2}")
	public int divide(@PathVariable int n1, @PathVariable int n2) {
		return service1.divide(n1, n2);
	}

	@GetMapping(path = "/report")
	public ReportDTO report() {
		return service2.reportComplessivo();
	}

	@GetMapping(path = "/report/{operation}")
	public ReportDTO statOperazione(@PathVariable String operation) {
		return service2.frequenzaSingolaOperazione(operation);
	}
}
