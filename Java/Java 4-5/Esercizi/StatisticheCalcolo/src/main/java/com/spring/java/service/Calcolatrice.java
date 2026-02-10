package com.spring.java.service;

import org.springframework.stereotype.Service;

@Service
public class Calcolatrice {

	public int add(int n1, int n2) {
		return n1 + n2;
	}

	public int subtract(int n1, int n2) {
		return n1 - n2;
	}

	public int multiply(int n1, int n2) {
		return n1 * n2;
	}

	public int divide(int n1, int n2) throws ArithmeticException {
		if (n2 != 0)
			return n1 / n2;
		throw new ArithmeticException();
	}
}
