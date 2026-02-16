package com.spring.java.dto;

import java.util.Objects;

public class ProductAndCredentialsDTO {
	private int id;
	private String name;
	private double price;
	private int stock;
	private String username;
	private String password;

	public ProductAndCredentialsDTO() {
	}

	public ProductAndCredentialsDTO(int id, String name, double price, int stock, String username, String password) {
		super();
		this.id = id;
		this.name = name;
		this.price = price;
		this.stock = stock;
		this.username = username;
		this.password = password;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		this.price = price;
	}

	public int getStock() {
		return stock;
	}

	public void setStock(int stock) {
		this.stock = stock;
	}

	@Override
	public int hashCode() {
		return Objects.hash(id);
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		ProductAndCredentialsDTO other = (ProductAndCredentialsDTO) obj;
		return id == other.id;
	}

	@Override
	public String toString() {
		return id + " | " + name + " | " + price + "€ | stock: " + stock;
	}
}
