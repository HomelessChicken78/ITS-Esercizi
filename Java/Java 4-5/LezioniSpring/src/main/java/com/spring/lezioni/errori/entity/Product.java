package com.spring.lezioni.errori.entity;

public class Product {
	private int prodId;
	private String name;

	public Product() {}
	
	public Product(int prodId, String name) {
		this.prodId = prodId;
		this.name = name;
	}

	public int getProdId() {
		return prodId;
	}

	public void setProdId(int prodId) {
		this.prodId = prodId;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
}
