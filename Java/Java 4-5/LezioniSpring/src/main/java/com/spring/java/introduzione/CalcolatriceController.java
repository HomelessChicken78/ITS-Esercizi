package com.spring.java.introduzione;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/calcolo")
public class CalcolatriceController {
	public CalcolatriceController() {
	}

	@GetMapping(path = "/somma")
	public int somma(int n1, int n2) {
		return n1 + n2;
	}
}
